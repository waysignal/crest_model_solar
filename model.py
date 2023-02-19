from inputs import *
from constants import *
import numpy_financial as npf

class Model():
    def __init__ (self,
    project_inputs = ProjectInputs(),
    capital_inputs = CapitalInputs(),
    om_inputs = OMInputs(),
    construction_inputs = ConstructionInputs(),
    pfin_inputs = PFinCosts(),
    tax_inputs = TaxInputs(),
    tariff_inputs = TariffInputs(20,1.0,0.02),
    forecasted_inputs = ForecastInputs(5,0.03),
    cost_fed_inc_inputs = CostFedIncInputs(True,0.26,1.0),
    capex_inverter_inputs= CapExInverterInputs(10,0.235,20,0.245),
    reserves_inputs = ReservesInput(False,0,6,6,0.02),
    depreciation_inputs = DepreciationInput(True,0.5)
    ):


        # Project Inputs
        self.proj_nameplate_capacity = project_inputs.nameplate_capacity
        self.proj_ncf_year_one = project_inputs.ncf_year_one
        self.proj_production = self.proj_nameplate_capacity * self.proj_ncf_year_one * 8760
        self.proj_annual_production_degradation = project_inputs.annual_production_degradation
        self.proj_project_useful_life = project_inputs.project_useful_life

        self.capital_generation_equipment= capital_inputs.generation_equipment
        self.capital_balance_of_plant= capital_inputs.balance_of_plant
        self.capital_interconnection= capital_inputs.interconnection
        self.capital_dev_costs= capital_inputs.dev_costs

        self.om_fixed_om_expense_yr_one= om_inputs.fixed_om_expense_yr_one
        self.om_variable_om_expense_yr_one= om_inputs.variable_om_expense_yr_one
        self.om_cost_inflation_initial= om_inputs.om_cost_inflation_initial
        self.om_initial_period_end= om_inputs.initial_period_end
        self.om_cost_inflation_subse= om_inputs.om_cost_inflation_subse
        self.om_insurance_yr_one_pc= om_inputs.insurance_yr_one_pc
        self.om_insurance_yr_one_dollars= self.om_insurance_yr_one_pc * (self.capital_generation_equipment \
                                        + self.capital_balance_of_plant \
                                        + self.capital_interconnection \
                                        + self.capital_dev_costs)
        self.om_project_management_yr_one= om_inputs.project_management_yr_one
        self.om_property_tax= om_inputs.property_tax
        self.om_annual_prop_tax_adjustment= om_inputs.annual_prop_tax_adjustment
        self.om_land_lease= om_inputs.land_lease
        self.om_royalties_pc= om_inputs.royalties_pc

        self.tariff_duration= tariff_inputs.tariff_duration
        self.tariff_pc_escalation= tariff_inputs.pc_escalation
        self.tariff_escalation_rate= tariff_inputs.pc_escalation_rate 
        self.forecasted_voe = forecasted_inputs.forecasted_value_of_energy
        self.forecasted_escal_rate = forecasted_inputs.forecasted_escal_rate

        self.pfin_pc_debt= pfin_inputs.pc_debt
        self.pfin_debt_term= pfin_inputs.debt_term
        self.pfin_debt_interest_rate= pfin_inputs.debt_interest_rate
        self.pfin_lender_fee= pfin_inputs.lender_fee
        self.pfin_required_min_dscr= pfin_inputs.required_min_dscr
        self.pfin_required_avg_dscr= pfin_inputs.required_avg_dscr
        self.pfin_target_after_tax_equity_irr= pfin_inputs.target_after_tax_equity_irr
        self.pfin_other_closing_costs= pfin_inputs.other_closing_costs
        self.summary_grants=0
        self.summary_senior_debt= self.pfin_pc_debt * (self.capital_generation_equipment \
                                                        + self.capital_balance_of_plant \
                                                        + self.capital_interconnection \
                                                        + self.capital_dev_costs) - self.summary_grants
        
        self.inverter_first_replacement= capex_inverter_inputs.first_replacement
        self.inverter_first_replacement_cost_watt= capex_inverter_inputs.first_replacement_cost
        self.inverter_second_replacement= capex_inverter_inputs.second_replacement
        self.inverter_second_replacement_cost_watt= capex_inverter_inputs.second_replacement_cost
        self.res_fund_from_operations= reserves_inputs.fund_from_operations
        self.res_reserve_req= reserves_inputs.reserve_req
        self.res_debt_service_req= reserves_inputs.debt_service_req
        self.res_om_wc_req= reserves_inputs.om_wc_req
        self.res_interest_on_reserves= reserves_inputs.interest_on_reserves
        self.res_debt_service_req_dollars= abs(npf.pmt(self.pfin_debt_interest_rate,  self.pfin_debt_term , self.summary_senior_debt)/12 * self.res_debt_service_req).round(0)
        self.results_coe = 28.05
        self.res_om_wc_req_dollars= abs((np.average(self.total_operating_expenses())/12 * self.res_om_wc_req).round(0))
        



    def production_degradation_factor(self):
        l = np.array([1.0])
        for i in range(1,self.proj_project_useful_life):
            l = np.append(l,(1-self.proj_annual_production_degradation) * l[i-1])
        return l
    
    def production(self):
        l = self.production_degradation_factor()
        return (l * self.proj_production).round(1)

    def operating_expense_inflation_factor(self):
        operation_expense_inflation_factor = np.array([1])
        for i in range(1,self.proj_project_useful_life):
            if i <= self.om_cost_inflation_initial:
                operation_expense_inflation_factor = np.append(operation_expense_inflation_factor,operation_expense_inflation_factor[i-1]*(1+self.om_cost_inflation_initial))
            else:
                operation_expense_inflation_factor = np.append(operation_expense_inflation_factor,operation_expense_inflation_factor[i-1]*(1+self.om_cost_inflation_subse))
        return operation_expense_inflation_factor
    
    def fixed_om_expense(self):
        l = self.operating_expense_inflation_factor()
        return -(l * self.om_fixed_om_expense_yr_one * self.proj_nameplate_capacity).round(0)

    def var_om_expense(self):
        l = self.operating_expense_inflation_factor()
        p = self.production()
        return -(l * p * self.om_variable_om_expense_yr_one/100).round(0)

    def insurance(self):
        l = self.operating_expense_inflation_factor()
        return -(self.om_insurance_yr_one_dollars * l).round(0)
    
    def project_management(self):
        l = self.operating_expense_inflation_factor()
        return -(self.om_project_management_yr_one * l).round(0)

    def property_taxes(self):
        l = np.array([self.om_property_tax])
        for i in range(1,self.proj_project_useful_life):
            l = np.append(l, (1 + self.om_annual_prop_tax_adjustment)* l[i-1])
        return -l.round(0)

    def land_lease(self):
        l = self.operating_expense_inflation_factor()
        return -(self.om_land_lease * l).round(0)

    def tariff_rate_total(self):
        tariff_rate_fixed= 1 - self.tariff_pc_escalation
        fixed_rate_arr = np.empty(self.tariff_duration); fixed_rate_arr.fill((tariff_rate_fixed * self.results_coe))
        escal_rate_arr = np.array([self.tariff_pc_escalation * self.results_coe])
        for i in range(1,self.tariff_duration):
            escal_rate_arr = np.append(escal_rate_arr, escal_rate_arr[i-1]*(1 + self.tariff_escalation_rate))
        total= (escal_rate_arr + fixed_rate_arr)
        return np.pad(total, (0, self.proj_project_useful_life - self.tariff_duration), 'constant')

    def revenue_from_tariff(self):
        return ((self.production() * self.tariff_rate_total())/100).round(0)

    def market_revenue(self):
        if self.tariff_duration < self.proj_project_useful_life:
            l = np.array([self.forecasted_voe])
            for i in range(1, self.proj_project_useful_life):
                l = np.append(l, l[i-1] * (1 + self.forecasted_escal_rate))
            l[:self.tariff_duration] = 0
            return (l * self.production()/100).round(0)
        else:
            return np.zeros(self.proj_project_useful_life)

    def royalties(self):
        return -(self.om_royalties_pc *  (self.revenue_from_tariff() + self.market_revenue())).round(0) 

    def total_operating_expenses(self):
        return self.fixed_om_expense() \
            + self.var_om_expense() \
            + self.insurance() \
            + self.project_management() \
            + self.property_taxes() \
            + self.land_lease() \
            + self.royalties()

    def reserve_accounts(self):
        l = np.array([0,self.res_debt_service_req_dollars, self.res_om_wc_req_dollars, 0, 0])
        l = np.append(l,np.sum(l))
        #Decommissioning Reserve
        df = pd.DataFrame(columns= range(self.proj_project_useful_life+1), index = ['Beginning Balance','Debt Service Reserve','O&M/Working Capital Reserve','Major Equipment Replacement Reserves','Decommissioning Reserve','Ending Balance'])
        df[0] = l
        for i in range(1,self.proj_project_useful_life+1):
            if (i == self.pfin_debt_term + 1):
                ds = -self.res_debt_service_req_dollars
            else:
                ds = 0 

            if (i == self.proj_project_useful_life):
                om = -self.res_om_wc_req_dollars
            else:
                om = 0

            if (i < self.inverter_first_replacement):
                e = (self.inverter_first_replacement_cost_watt * self.proj_nameplate_capacity)/(self.inverter_first_replacement - 1) * 1000

            elif ( i == self.inverter_first_replacement): 
                e = -self.inverter_first_replacement_cost_watt * self.proj_nameplate_capacity * 1000
            elif ( i < self.inverter_second_replacement):
                e = (self.inverter_second_replacement_cost_watt * self.proj_nameplate_capacity)/(self.inverter_second_replacement - self.inverter_first_replacement - 1) * 1000
                
            elif ( i == self.inverter_second_replacement):
                e = -self.inverter_second_replacement_cost_watt * self.proj_nameplate_capacity * 1000
            else: 
                e = 0
            d = np.array([df.loc['Ending Balance'][i-1],ds,om,e,0])
            d = np.append(d,np.sum(d))
            df[i] = d

        df = df.astype('int')
        return df

    def interest_on_reserves(self):
        df = self.reserve_accounts()
        l = np.array([])
        for i in range(1,self.proj_project_useful_life + 1):
            l = (np.append(l, (df.loc['Beginning Balance'][i] + df.loc['Ending Balance'][i])/2 * self.res_interest_on_reserves)).round(0)
        return l
        
    def project_revenue_all(self):
        return self.revenue_from_tariff() + self.market_revenue() + self.interest_on_reserves()


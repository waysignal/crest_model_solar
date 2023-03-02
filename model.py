from inputs import *
from constants import *
import numpy_financial as npf
from pandas.testing import assert_series_equal

class Model():
    def __init__ (self,
    project_inputs = ProjectInputs(),
    capital_inputs = CapitalInputs(),
    om_inputs = OMInputs(),
    construction_inputs = ConstructionInputs(),
    pfin_inputs = PFinCosts(),
    tax_inputs = TaxInputs(),
    tariff_inputs = TariffInputs(),
    forecasted_inputs = ForecastInputs(),
    cost_fed_inc_inputs = CostFedIncInputs(),
    cost_state_inc_inputs = CostStateIncInputs(),
    capex_inverter_inputs= CapExInverterInputs(),
    reserves_inputs = ReservesInput(),
    depreciation_inputs = DepreciationInput(),
    fed_pbi_inputs = CostFedIncInputsPerf(),
    state_pbi_inputs = CostStateIncInputsPerf()
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
        self.inverter_first_replacement= capex_inverter_inputs.first_replacement
        self.inverter_first_replacement_cost_watt= capex_inverter_inputs.first_replacement_cost
        self.inverter_second_replacement= capex_inverter_inputs.second_replacement
        self.inverter_second_replacement_cost_watt= capex_inverter_inputs.second_replacement_cost
        self.res_fund_from_operations= reserves_inputs.fund_from_operations
        self.res_reserve_req= reserves_inputs.reserve_req
        self.res_debt_service_req= reserves_inputs.debt_service_req
        self.res_om_wc_req= reserves_inputs.om_wc_req
        self.res_interest_on_reserves= reserves_inputs.interest_on_reserves
        
        
        self.construction_period= construction_inputs.construction_period
        self.construction_interest_rate= construction_inputs.construction_interest_rate
        self.construction_interest_dollars= (self.capital_generation_equipment \
                                            + self.capital_balance_of_plant \
                                            + self.capital_interconnection \
                                            + self.capital_dev_costs) \
                                            * (self.construction_interest_rate / 12) \
                                            * (self.construction_period / 2) 
        
        self.fincent_fed_itc_or_cash= cost_fed_inc_inputs.itc_or_cash
        self.fincent_fed_itc_amount= cost_fed_inc_inputs.itc_amount
        self.fincent_fed_itc_utilization_factor= cost_fed_inc_inputs.itc_utilization_factor
        self.fincent_fed_itc_or_cash_grant_dollar= cost_fed_inc_inputs.itc_or_cash_dollar
        self.fincent_fed_additional_grants = cost_fed_inc_inputs.fed_additional_grants
        self.fincent_fed_form = cost_fed_inc_inputs.fed_form

        self.fincent_state_itc_amount= cost_state_inc_inputs.itc_amount
        self.fincent_state_itc_utilization_factor= cost_state_inc_inputs.itc_utilization_factor
        self.fincent_state_itc_or_cash_grant_dollar= cost_state_inc_inputs.itc_or_cash_dollar
        self.fincent_state_realization_period= cost_state_inc_inputs.itc_realization_period
        self.fincent_state_additional_grants = cost_state_inc_inputs.state_additional_grants
        self.fincent_state_form = cost_state_inc_inputs.state_form

        self.dep_bonus_depreciation= depreciation_inputs.bonus_depreciation
        self.dep_bonus_depreciation_pc= depreciation_inputs.bonus_depreciation_pc
        self.depreciation_allocation_table = depreciation_allocation_table()
        self.tax_fed_income_tax_rate= tax_inputs.fed_income_tax_rate
        self.tax_fed_generated= tax_inputs.fed_generated
        self.tax_state_income_tax_rate= tax_inputs.state_income_tax_rate
        self.tax_state_generated= tax_inputs.state_generated
        
        self.fed_ptc_or_repi= fed_pbi_inputs.ptc_or_repi
        self.fed_pbi_rate= fed_pbi_inputs.pbi_rate
        self.fed_pbi_util_rate = fed_pbi_inputs.pbi_util_rate
        self.fed_pbi_duration= fed_pbi_inputs.pbi_duration
        self.fed_pbi_escalation_rate= fed_pbi_inputs.pbi_escalation_rate
        
        self.state_cash_or_taxit= state_pbi_inputs.cash_or_taxit
        self.state_pbi_cap = state_pbi_inputs.pbi_cap
        self.state_pbi_rate= state_pbi_inputs.pbi_rate
        self.state_pbi_util_rate = state_pbi_inputs.pbi_util_rate
        self.state_pbi_duration= state_pbi_inputs.pbi_duration
        self.state_pbi_escalation_rate= state_pbi_inputs.pbi_escalation_rate
        self.state_total_cap = state_pbi_inputs.total_cap
        self.results_coe = 0
        self.res_om_wc_req_dollars= abs((np.average(self.total_operating_expenses())/12 * self.res_om_wc_req).round(0))

        self.summary_grants= self.fincent_fed_additional_grants * (1- self.tax_fed_income_tax_rate) +\
                               (0 if self.fincent_state_additional_grants == 0 else  \
                               (self.fincent_state_additional_grants * 1000 * self.proj_nameplate_capacity) * ( 1 - self.tax_state_income_tax_rate) if self.state_total_cap == 0 else \
                                min((self.fincent_state_additional_grants * 1000 * self.proj_nameplate_capacity) * ( 1 - self.tax_state_income_tax_rate), self.state_total_cap*(1 - self.tax_state_income_tax_rate) ))
        self.summary_senior_debt= self.pfin_pc_debt * (self.capital_generation_equipment \
                                                        + self.capital_balance_of_plant \
                                                        + self.capital_interconnection \
                                                        + self.capital_dev_costs) - self.summary_grants
        self.res_debt_service_req_dollars= abs(npf.pmt(self.pfin_debt_interest_rate,  self.pfin_debt_term , self.summary_senior_debt)/12 * self.res_debt_service_req).round(0)
        self.capital_reserves_financing_costs= self.pfin_lender_fee * self.pfin_pc_debt * (self.capital_generation_equipment \
                                                                            + self.capital_balance_of_plant \
                                                                            + self.capital_interconnection \
                                                                            + self.capital_dev_costs) \
                                    + self.construction_interest_dollars \
                                    + self.pfin_other_closing_costs \
                                    + self.res_debt_service_req_dollars + self.res_om_wc_req_dollars
        self.capital_total_installed_cost= (self.capital_generation_equipment \
                                        + self.capital_balance_of_plant \
                                        + self.capital_interconnection \
                                        + self.capital_dev_costs) \
                                        + self.capital_reserves_financing_costs
        self.capital_total_install_costs_watt= self.capital_total_installed_cost / self.proj_nameplate_capacity / 1000 
        
       
        self.summary_equity= self.capital_total_installed_cost  - self.summary_grants - self.summary_senior_debt
        self.helper_irr = 0
        self.fed_itc_or_cash_grant_dollars= 0
        self.state_itc_or_cash_grant_dollars= 0

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
        return -(self.om_royalties_pc *  (self.revenue_from_tariff() + self.market_revenue() + self.federal_cash_incentive() + self.state_cash_incentive())).round(0) 

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
            d = np.array([df.loc['Ending Balance'][i-1],ds,om,e,0 if self.res_fund_from_operations == False else self.res_reserve_req/self.proj_project_useful_life])
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
        return self.revenue_from_tariff() + self.market_revenue() + self.interest_on_reserves() + self.federal_cash_incentive() + self.state_cash_incentive()

    def ebitda(self):
        return self.project_revenue_all() + self.total_operating_expenses()

    def loan_interest(self):
        l = np.array([])
        for i in range(0,self.pfin_debt_term):
            l = np.append(l,npf.ipmt(self.pfin_debt_interest_rate,i+1,  self.pfin_debt_term , self.summary_senior_debt))
        return np.pad(l, (0, self.proj_project_useful_life - self.pfin_debt_term), 'constant').round(0)
       
    def operating_income_after_interest_expense(self):
        return self.ebitda() + self.loan_interest()

    def loan_principal(self):
        l = np.array([])
        for i in range(0,self.pfin_debt_term):
            l = np.append(l,npf.ppmt(self.pfin_debt_interest_rate,i+1,  self.pfin_debt_term , self.summary_senior_debt))
        return np.pad(l, (0, self.proj_project_useful_life - self.pfin_debt_term), 'constant').round(0)
    
    def annual_conliq_reserves(self):
        df = self.reserve_accounts()
        l = df.iloc[1:5,1:] #['Debt Service Reserve','O&M/Working Capital Reserve','Major Equipment Replacement Reserves','Decommissioning Reserve']
        l.loc['Total',:]= l.sum(axis=0)
        l = l.astype('int')
        return l.loc['Total'].to_numpy()

    def adjustments_major_equipment(self):
        df = self.reserve_accounts()
        major = df.iloc[3, 1:].to_numpy()
        zero = np.zeros(self.proj_project_useful_life)
        return np.minimum(zero,major)

    def pretax_cash_flow_to_equity(self):
        return self.operating_income_after_interest_expense() + self.loan_principal() - self.annual_conliq_reserves() + self.adjustments_major_equipment()
    
    def equity_investment(self):
        l = np.array([-self.summary_equity])
        return np.pad(l, (0, self.proj_project_useful_life), 'constant')

    def net_pretax_cash_flow_to_equity(self):
        p = np.insert(self.pretax_cash_flow_to_equity(), 0 , 0)
        return self.equity_investment() + p
    
    def fed_itc_or_cash_grant(self, five_year_macrs):
            if self.fincent_fed_form == 'Cost':
                g = self.fincent_fed_itc_amount * self.fincent_fed_itc_utilization_factor * five_year_macrs
                return g 
            else:
                return 0 * five_year_macrs
            
    def state_itc_or_cash_grant(self, five_year_macrs):
        if self.fincent_state_form== 'Cost':
            g = self.fincent_state_itc_amount * self.fincent_state_itc_utilization_factor * (1 - self.tax_fed_income_tax_rate) * five_year_macrs
            return g 
        else:
            return 0 * five_year_macrs

    def annual_depreciation_expense(self):
        t = self.depreciation_allocation_table
        costs = np.array([self.capital_generation_equipment, self.capital_balance_of_plant, self.capital_interconnection, self.capital_dev_costs, self.capital_reserves_financing_costs])
        l = np.array([])
        for i in range(len(t.columns)):
            l = np.append(l,(sum(t.iloc[:,i].to_numpy() * costs)))

        df = pd.DataFrame(l, index = ['5-year MACRS','7-year MACRS','15-year MACRS', '20-year MACRS', '5-year SL', '15-year SL', '20-year SL', '39-year SL', 'Non-Depreciable'], \
                                    columns = ['Before Adjustments' ])
        
        project_cost_basis = sum(l)
        self.fed_itc_or_cash_grant_dollars = self.fed_itc_or_cash_grant(df.iloc[0,0])
        self.state_itc_or_cash_grant_dollars = self.state_itc_or_cash_grant(df.iloc[0,0])       
      
        adjustments = 0.5 * self.fed_itc_or_cash_grant_dollars
        allocation = np.array([])
        for i in range(len(df.index)):
            allocation = np.append(allocation, df.iloc[i,0] / project_cost_basis)
        df['Allocation'] = allocation.round(2)
        bonus_pc = (1 - self.dep_bonus_depreciation_pc) if self.dep_bonus_depreciation == True else 1.0
        after_adjustments = (project_cost_basis - adjustments) * bonus_pc * allocation
        bonus_depreciation = np.array([0,0,(project_cost_basis - adjustments) * (0 if self.dep_bonus_depreciation == False else self.dep_bonus_depreciation_pc)])
        df['After Adjustments'] = after_adjustments
        df.loc['Bonus Depreciation'] = bonus_depreciation
        df = df.reindex(index = ['5-year MACRS','7-year MACRS','15-year MACRS', '20-year MACRS', '5-year SL', '15-year SL', '20-year SL', '39-year SL', 'Bonus Depreciation' ,'Non-Depreciable'])

        df2 = depreciation_schedule_table()
        df3 = df2.multiply(df.iloc[:-1,2].to_numpy(), axis =0)
        assert_series_equal(df3.sum(axis = 1), df.iloc[:-1,2].rename(None))
    
        first_replacement_cost= self.inverter_first_replacement_cost_watt * self.proj_nameplate_capacity * 1000
        second_replacement_cost = self.inverter_second_replacement_cost_watt * self.proj_nameplate_capacity * 1000

        first_depreciation_expense = np.array([])
        second_depreciation_expense = np.array([])

        for i in range(1,31):
            if i >= self.inverter_first_replacement:
                first_depreciation_expense = np.append(first_depreciation_expense, first_replacement_cost * df2.iloc[0, int(i - (self.inverter_first_replacement -1))-1] )
            else :
                first_depreciation_expense = np.append(first_depreciation_expense, 0)
            if i >= self.inverter_second_replacement:
                second_depreciation_expense = np.append(second_depreciation_expense, second_replacement_cost * df2.iloc[0, int(i - (self.inverter_second_replacement -1))-1] )
            else :
                second_depreciation_expense = np.append(second_depreciation_expense, 0)

        return (df3.sum(axis=0) + first_depreciation_expense + second_depreciation_expense).to_numpy()[:self.proj_project_useful_life].round(0)
    
    def taxable_income(self):
        return self.operating_income_after_interest_expense() - self.annual_depreciation_expense()
    
    def taxable_income_with_carry_forward(self):
        t = self.taxable_income()
        df = pd.DataFrame(
                        index = ['Operating Loss Carry-Forward',\
                                'Additional Operating Loss Carried-Forward',\
                                'Utilization of Operating Loss Carry-Forward',\
                                'Operating Loss Carry-Forward, Ending Balance'])
        for i in range(t.size):
            l = np.array([0 if i == 0 else df.iloc[3,i-1] , 0 if t[i] > 0 else -t[i] , 0 if t[i] <= 0 else -min(t[i], 0 if i == 0 else df.iloc[3,i-1] )])
            l = np.append(l,np.sum(l))
            df[i+1] = l

        return (t + df.loc['Additional Operating Loss Carried-Forward'] + df.loc['Utilization of Operating Loss Carry-Forward']).to_numpy()
        
    def federal_tax_credit_benefits(self):
        fed_itc_as_generated = np.array([])
        fed_ptc_as_generated = np.array([])
        fed_income_taxes_saved_before_credit = np.array([])
        p = self.production()
    
        for i in range(1,self.proj_project_useful_life+1):
            if i == 1 & self.fincent_fed_itc_or_cash == True:
                fed_itc_as_generated = np.append(fed_itc_as_generated,self.fed_itc_or_cash_grant_dollars)
            else:
                fed_itc_as_generated = np.append(fed_itc_as_generated,0)
        
            if self.fincent_fed_form == 'Performance' and self.fed_ptc_or_repi == 'PTC' and i <= self.fed_pbi_duration:
                fed_ptc_as_generated = np.append(fed_ptc_as_generated,(self.fed_pbi_rate / 100) * self.fed_pbi_util_rate * pow((1 + self.fed_pbi_escalation_rate), i-1) * p[i-1] * (1 - min(0.5, self.fincent_fed_additional_grants / self.capital_total_installed_cost)))
            else: 
                fed_ptc_as_generated = np.append(fed_ptc_as_generated,0)

        applicable_tax_credits = fed_itc_as_generated + fed_ptc_as_generated
        state_income_taxes_saved_before_credit = -(self.taxable_income_state()- 0 ) * self.tax_state_income_tax_rate
        fed_income_taxes_saved_before_credit = -(self.taxable_income_federal() + state_income_taxes_saved_before_credit) *  self.tax_fed_income_tax_rate
            
        df = pd.DataFrame(
        index = ['Applicable Tax Credits, as generated',\
                'Tax Benefit Carry-Forward, Beginning Balance',\
                'Additional Tax Benefit Carry-Forward',\
                'Utilization of Tax Benefit Carry-Forward',\
                'Tax Benefit Carry-Forward, Ending Balance'])
            
        for i in range(applicable_tax_credits.size):
            l = np.array([applicable_tax_credits[i], 0 if i == 0 else df.iloc[4,i-1] ,\
                        0 if self.tax_fed_generated == True else (applicable_tax_credits[i] if fed_income_taxes_saved_before_credit[i] <= 0 else 0 ),\
                        0 if self.tax_fed_generated == True else (max(fed_income_taxes_saved_before_credit[i], -(applicable_tax_credits[i] if fed_income_taxes_saved_before_credit[i] <= 0 else 0) if i == 0 else -df.iloc[4,i-1] )   if fed_income_taxes_saved_before_credit[i] < 0    else 0),\
                        ])
            l = np.append(l,np.sum(l[1:]))
            df[i+1] = l
        df.loc['Federal Income Taxes Saved / (Paid), before ITC/PTC',:] = fed_income_taxes_saved_before_credit
        df.loc['State Income Taxes Saved / (Paid), before ITC/PTC',:] = state_income_taxes_saved_before_credit
        return df.round(0)
        
    def state_tax_credit_benefits(self):
        state_itc_as_generated = np.array([])
        state_ptc_as_generated = np.array([])
        state_income_taxes_saved_before_credit = np.array([])
        p = self.production()
        for i in range(1,self.proj_project_useful_life+1):
            if i <= self.fincent_state_realization_period and self.fincent_state_form == 'Cost' :
                state_itc_as_generated = np.append(state_itc_as_generated, self.state_itc_or_cash_grant_dollars/ self.fincent_state_realization_period)
            else:
                state_itc_as_generated = np.append(state_itc_as_generated,0)
            
            if self.fincent_state_form == 'Performance' and self.state_cash_or_taxit == 'Tax Credit' and i <= self.state_pbi_duration:

                state_ptc_as_generated = np.append(state_ptc_as_generated,(self.state_pbi_rate / 100) * self.state_pbi_util_rate * pow((1 + self.state_pbi_escalation_rate), i-1) * p[i-1] * (1 - min(0.5, self.fincent_fed_additional_grants/ self.capital_total_installed_cost)))
            else: 
                state_ptc_as_generated = np.append(state_ptc_as_generated,0)

        applicable_tax_credits = state_itc_as_generated + state_ptc_as_generated
        state_income_taxes_saved_before_credit = -(self.taxable_income_state() - 0 ) * self.tax_state_income_tax_rate
        fed_income_taxes_saved_before_credit = -(self.taxable_income_federal() + state_income_taxes_saved_before_credit) *  self.tax_fed_income_tax_rate
        df = pd.DataFrame(
        index = ['Applicable Tax Credits, as generated',\
                'Tax Benefit Carry-Forward, Beginning Balance',\
                'Additional Tax Benefit Carry-Forward',\
                'Utilization of Tax Benefit Carry-Forward',\
                'Tax Benefit Carry-Forward, Ending Balance'])
        for i in range(applicable_tax_credits.size):
            l = np.array([applicable_tax_credits[i], 0 if i == 0 else df.iloc[4,i-1] ,\
                        0 if self.tax_state_generated == True else (applicable_tax_credits[i] if state_income_taxes_saved_before_credit[i] <= 0 else 0 ),\
                        0 if self.tax_state_generated == True else (max(state_income_taxes_saved_before_credit[i], -(applicable_tax_credits[i] if state_income_taxes_saved_before_credit[i] <= 0 else 0) if i == 0 else -df.iloc[4,i-1] )   if state_income_taxes_saved_before_credit[i] < 0    else 0),\
                        ])
            l = np.append(l,np.sum(l[1:]))
            df[i+1] = l
        df.loc['Federal Income Taxes Saved / (Paid), before ITC/PTC',:] = fed_income_taxes_saved_before_credit
        df.loc['State Income Taxes Saved / (Paid), before ITC/PTC',:] = state_income_taxes_saved_before_credit
        return df.round(0)
   
    
    def after_tax_cash_flow_to_equity(self):
        df = self.federal_tax_credit_benefits()
        r = (df.loc['Federal Income Taxes Saved / (Paid), before ITC/PTC']+ df.loc['State Income Taxes Saved / (Paid), before ITC/PTC']).to_numpy()\
            + self.cash_benefit_federal() + (self.cash_benefit_state() if self.fincent_state_form != 'Neither' else np.zeros(25))
        r = np.insert(r, 0 , 0)
        return self.net_pretax_cash_flow_to_equity() + r

    def irr_arr(self):
        cf = self.after_tax_cash_flow_to_equity()
        l = np.array([])
        for i in range(1, cf.size):
            l = np.append(l,npf.irr(cf[:i+1]))
        return l.round(3)

    def irr(self):
        cf = self.after_tax_cash_flow_to_equity()
        return npf.irr(cf)

    def npv(self):
        return npf.npv(self.pfin_target_after_tax_equity_irr,self.after_tax_cash_flow_to_equity()).round(0)
    
    def find_coe(self):
        #self.results_coe = 27.85; self.refresh(); return self.results_coe
        coe_hold = 0
        for i in range(0,11):
            coe = 10 * i
            self.results_coe = coe
            self.refresh()
            npv = self.npv()
            if npv >= 0:
                coe_hold = (i-1) * 10
                break
        for i in range(0,11):
            coe = coe_hold + i 
            self.results_coe = coe
            self.refresh()
            npv = self.npv()
            if npv >= 0:
                coe_hold = coe_hold + (i-1)
                break
        for i in range(0,11):
            coe = coe_hold + i / 10
            self.results_coe = coe
            self.refresh()
            npv = self.npv()
            if npv >= 0:
                coe_hold = coe_hold + (i-1) /10 
                break
        self.results_coe = (coe_hold *2 + 0.1 )/2
        self.refresh()
        return self.results_coe
    

    def refresh(self):
        self.summary_grants= self.fincent_fed_additional_grants * (1- self.tax_fed_income_tax_rate) +\
                                (0 if self.fincent_state_additional_grants == 0 else (self.fincent_state_additional_grants * 1000 * self.proj_nameplate_capacity) * ( 1 - self.tax_state_income_tax_rate) if self.state_total_cap == 0 else \
                                min((self.fincent_state_additional_grants * 1000 * self.proj_nameplate_capacity) * ( 1 - self.tax_state_income_tax_rate), self.state_total_cap*(1 - self.tax_state_income_tax_rate) ))
        self.summary_senior_debt= self.pfin_pc_debt * (self.capital_generation_equipment \
                                                        + self.capital_balance_of_plant \
                                                        + self.capital_interconnection \
                                                        + self.capital_dev_costs - self.summary_grants)
        
        self.res_debt_service_req_dollars= abs(npf.pmt(self.pfin_debt_interest_rate,  self.pfin_debt_term , self.summary_senior_debt)/12 * self.res_debt_service_req).round(0)
        self.res_om_wc_req_dollars= abs((np.average(self.total_operating_expenses())/12 * self.res_om_wc_req).round(0))
        self.capital_reserves_financing_costs= self.pfin_lender_fee * self.pfin_pc_debt * (self.capital_generation_equipment \
                                                                            + self.capital_balance_of_plant \
                                                                            + self.capital_interconnection \
                                                                            + self.capital_dev_costs) \
                                    + self.construction_interest_dollars \
                                    + self.pfin_other_closing_costs \
                                    + self.res_debt_service_req_dollars + self.res_om_wc_req_dollars
        self.capital_total_installed_cost= (self.capital_generation_equipment \
                                        + self.capital_balance_of_plant \
                                        + self.capital_interconnection \
                                        + self.capital_dev_costs) \
                                        + self.capital_reserves_financing_costs \
                                        
        self.capital_total_install_costs_watt= self.capital_total_installed_cost / self.proj_nameplate_capacity / 1000 
        self.summary_equity= self.capital_total_installed_cost  - self.summary_grants - self.summary_senior_debt


    def cash_benefit_federal(self):
        df = self.federal_tax_credit_benefits()
        if self.fincent_fed_itc_or_cash == False and self.fincent_fed_form == 'Cost':
            return np.append([self.fed_itc_or_cash_grant_dollars], -df.loc['Utilization of Tax Benefit Carry-Forward',2:]) 
        elif self.tax_fed_generated == True:
            return df.loc['Applicable Tax Credits, as generated'].to_numpy()
        else:
            return -df.loc['Utilization of Tax Benefit Carry-Forward'].to_numpy()
    
    def cash_benefit_state(self):
        df = self.state_tax_credit_benefits()
        if self.tax_state_generated == True:
            return df.loc['Applicable Tax Credits, as generated'].to_numpy()
        else:
            return -df.loc['Utilization of Tax Benefit Carry-Forward'].to_numpy()
            
    
    def taxable_income_federal(self):
        if self.tax_fed_generated == True:
            return self.taxable_income()
        else:
            return self.taxable_income_with_carry_forward() 
        
    def taxable_income_state(self):
        if self.tax_state_generated == True:
            return self.taxable_income()
        else:
            return self.taxable_income_with_carry_forward()
    
    def federal_cash_incentive(self):
        if self.fincent_fed_form == 'Performance' and self.fed_ptc_or_repi == 'REPI':
            fed_cash_incentive_rate = np.array([self.fed_pbi_rate])
            for i in range(1,self.fed_pbi_duration):
                fed_cash_incentive_rate = np.append(fed_cash_incentive_rate, fed_cash_incentive_rate[i-1]*(1 + self.fed_pbi_escalation_rate))
            fed_cash_incentive_rate = np.pad(fed_cash_incentive_rate,(0, self.proj_project_useful_life - self.fed_pbi_duration), 'constant')
        else :
            fed_cash_incentive_rate = np.pad(0,self.proj_project_useful_life,'constant')
        return (fed_cash_incentive_rate * self.production() /100).round(0)

    def state_cash_incentive(self):
        if self.fincent_state_form == 'Performance' and self.state_cash_or_taxit == 'Cash':
            state_cash_incentive_rate = np.array([self.state_pbi_rate])
            for i in range(1,self.state_pbi_duration):
                state_cash_incentive_rate = np.append(state_cash_incentive_rate, state_cash_incentive_rate[i-1]*(1 + self.state_pbi_escalation_rate))
            state_cash_incentive_rate = np.pad(state_cash_incentive_rate,(0, self.proj_project_useful_life - self.state_pbi_duration), 'constant')
        else :
            state_cash_incentive_rate = np.pad(0,self.proj_project_useful_life,'constant')
        return (state_cash_incentive_rate * self.production() /100).round(0) if self.state_pbi_cap == 0 else min (self.state_pbi_cap ,(state_cash_incentive_rate * self.production() /100).round(0) )
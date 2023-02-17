from inputs import *
from constants import *
import numpy_financial as npf

class Model():
    def __init__ (self,
    project_inputs = ProjectInputs(2200, 0.180456458333333, 0.005, 25),
    capital_inputs = CapitalInputs(),
    om_inputs = OMInputs(),
    construction_inputs = ConstructionInputs(6, 0.05),
    pfin_inputs = PFinCosts(0.45,18,0.07,0.03,1.20,1.45,0.15,0),
    tax_inputs = TaxInputs(True,0.35,False,0.085,False),
    tariff_inputs = TariffInputs(20,1.0,0.02),
    forecasted_inputs = ForecastInputs(5,0.03),
    cost_fed_inc_inputs = CostFedIncInputs(True,0.26,1.0),
    capex_inverter_inputs= CapExInverterInputs(10,0.235,20,0.235),
    reserves_inputs = ReservesInput(False,0,6,6,0.02),
    depreciation_inputs = DepreciationInput(True,0.5)
    ):


        # Project Inputs
        self.proj_nameplate_capacity = project_inputs.nameplate_capacity
        self.proj_ncf_year_one = project_inputs.ncf_year_one
        self.proj_production = self.proj_nameplate_capacity * self.proj_ncf_year_one * 8760
        self.proj_annual_production_degradation = project_inputs.annual_production_degradation
        self.proj_project_useful_life = project_inputs.project_useful_life

        # Capital Inputs
        self.capital_generation_equipment= capital_inputs.generation_equipment
        self.capital_balance_of_plant= capital_inputs.balance_of_plant
        self.capital_interconnection= capital_inputs.interconnection
        self.capital_dev_costs= capital_inputs.dev_costs

        # O&M Inputs
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

        


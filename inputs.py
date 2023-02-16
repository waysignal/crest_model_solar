class ProjectInputs:
    def __init__(self, 
                nameplate_capacity: int = 2200, 
                ncf_yr_one: float = 0.18, 
                annual_production_degradation: int = 0.005, 
                project_useful_life: int = 25):
        self.nameplate_capacity = nameplate_capacity
        self.ncf_year_one = ncf_yr_one
        self.annual_production_degradation = annual_production_degradation
        self.project_useful_life = project_useful_life

class CapitalInputs:
    def __init__(self,
                generation_equipment: int = 2000000,
                balance_of_plant: int = 2000000,
                interconnection: int = 500000,
                dev_costs: int = 1000000):
        self.generation_equipment= generation_equipment
        self.balance_of_plant= balance_of_plant
        self.interconnection= interconnection
        self.dev_costs= dev_costs


class OMInputs:
    def __init__(self,
                fixed_om_expense_yr_one: float = 5.00,
                variable_om_expense_yr_one: float = 0.0,
                om_cost_inflation_initial: float = 0.016,
                initial_period_end: int = 10,
                om_cost_inflation_subse: float = 0.016,
                insurance_yr_one_pc: float = 0.005,
                project_management_yr_one: int = 50000,
                property_tax: int = 50000,
                annual_prop_tax_adjustment: float = -0.1,
                land_lease: int = 5000,
                royalties_pc: float = 0.03):
        self.fixed_om_expense_yr_one= fixed_om_expense_yr_one
        self.variable_om_expense_yr_one= variable_om_expense_yr_one
        self.om_cost_inflation_initial= om_cost_inflation_initial
        self.initial_period_end= initial_period_end
        self.om_cost_inflation_subse= om_cost_inflation_subse
        self.insurance_yr_one_pc= insurance_yr_one_pc
        self.project_management_yr_one= project_management_yr_one
        self.property_tax= property_tax
        self.annual_prop_tax_adjustment= annual_prop_tax_adjustment
        self.land_lease= land_lease
        self.royalties_pc= royalties_pc

class ConstructionInputs:
        def __init__(self,
                construction_period: int, 
                construction_interest_rate: float,
                ):
                self.construction_period= construction_period
                self.construction_interest_rate= construction_interest_rate

class PFinCosts:
        def __init__(self,
                pc_debt: float,
                debt_term: int,
                debt_interest_rate: float,
                lender_fee: float,
                required_min_dscr: float,
                required_avg_dscr: float,
                target_after_tax_equity_irr: float,
                other_closing_costs: int):
                self.pc_debt= pc_debt
                self.debt_term= debt_term
                self.debt_interest_rate= debt_interest_rate
                self.lender_fee= lender_fee
                self.required_min_dscr= required_min_dscr
                self.required_avg_dscr= required_avg_dscr
                self.target_after_tax_equity_irr= target_after_tax_equity_irr
                self.other_closing_costs= other_closing_costs

class TaxInputs:
        def __init__(self,
                taxable: bool,
                fed_income_tax_rate: float,
                fed_generated: bool,
                state_income_tax_rate: float,
                state_generated: bool):
                self.taxable= taxable
                self.fed_income_tax_rate= fed_income_tax_rate
                self.fed_generated= fed_generated
                self.state_income_tax_rate= state_income_tax_rate
                self.state_generated= state_generated

class TariffInputs:
        def __init__(self,
                tariff_duration: int,
                pc_escalation: float,
                pc_escalation_rate: float):
                self.tariff_duration= tariff_duration
                self.pc_escalation= pc_escalation
                self.pc_escalation_rate= pc_escalation_rate 

class ForecastInputs:
        def __init__(self,
                forecasted_value_of_energy= 5.0,
                forecasted_escal_rate= 0.03):
                self.forecasted_value_of_energy= forecasted_value_of_energy
                self.forecasted_escal_rate= forecasted_escal_rate
class CostFedIncInputs:
        def __init__(self,
                itc_or_cash: bool,
                itc_amount: float,
                itc_utilization_factor: float):
                self.itc_or_cash= itc_or_cash
                self.itc_amount= itc_amount
                self.itc_utilization_factor= itc_utilization_factor

class CapExInverterInputs:
        def __init__(self,
                first_replacement: int,
                first_replacement_cost: float,
                second_replacement: int,
                second_replacement_cost: float):
                self.first_replacement= first_replacement
                self.first_replacement_cost= first_replacement_cost
                self.second_replacement= second_replacement
                self.second_replacement_cost= second_replacement_cost

class ReservesInput:
        def __init__(self,
                fund_from_operations: bool,
                reserve_req: int,
                debt_service_req: int,
                om_wc_req: int,
                interest_on_reserves: float):
                self.fund_from_operations= fund_from_operations
                self.reserve_req= reserve_req
                self.debt_service_req= debt_service_req
                self.om_wc_req= om_wc_req
                self.interest_on_reserves= interest_on_reserves

class DepreciationInput:
        def __init__(self,
                bonus_depreciation: bool,
                bonus_depreciation_pc: float):
                self.bonus_depreciation= bonus_depreciation
                self.bonus_depreciation_pc= bonus_depreciation_pc
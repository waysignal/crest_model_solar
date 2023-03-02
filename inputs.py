class ProjectInputs:
    def __init__(self, 
                nameplate_capacity: int = 2200, 
                ncf_yr_one: float = 0.180456458333333, 
                annual_production_degradation: int = 0.005, 
                project_useful_life: int = 25):
        self.nameplate_capacity = nameplate_capacity
        self.ncf_year_one = ncf_yr_one
        self.annual_production_degradation = annual_production_degradation
        self.project_useful_life = project_useful_life

class CapitalInputs:
    def __init__(self,
                generation_equipment: int = 2_000_000,
                balance_of_plant: int = 2_000_000,
                interconnection: int = 500_000,
                dev_costs: int = 1_000_000):
        self.generation_equipment= generation_equipment
        self.balance_of_plant= balance_of_plant
        self.interconnection= interconnection
        self.dev_costs= dev_costs


class OMInputs:
    def __init__(self,
                fixed_om_expense_yr_one: float = 5.00,
                variable_om_expense_yr_one: float = 0.01,
                om_cost_inflation_initial: float = 0.016,
                initial_period_end: int = 10,
                om_cost_inflation_subse: float = 0.016,
                insurance_yr_one_pc: float = 0.005,
                project_management_yr_one: int = 50_000,
                property_tax: int = 50_000,
                annual_prop_tax_adjustment: float = -0.1,
                land_lease: int = 5_000,
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
                construction_period: int = 6, 
                construction_interest_rate: float = 0.05,
                ):
                self.construction_period= construction_period
                self.construction_interest_rate= construction_interest_rate

class PFinCosts:
        def __init__(self,
                pc_debt: float = 0.45,
                debt_term: int = 18,
                debt_interest_rate: float = 0.07,
                lender_fee: float = 0.03,
                required_min_dscr: float = 1.20,
                required_avg_dscr: float = 1.45,
                target_after_tax_equity_irr: float = 0.15,
                other_closing_costs: int = 0):
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
                taxable: bool = True,
                fed_income_tax_rate: float = 0.35,
                fed_generated: bool = False,
                state_income_tax_rate: float = 0.085,
                state_generated: bool = False):
                self.taxable= taxable
                self.fed_income_tax_rate= fed_income_tax_rate
                self.fed_generated= fed_generated
                self.state_income_tax_rate= state_income_tax_rate
                self.state_generated= state_generated

class TariffInputs:
        def __init__(self,
                tariff_duration: int = 20,
                pc_escalation: float = 1.0,
                pc_escalation_rate: float = 0.02):
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
                itc_or_cash: bool = True,
                itc_amount: float = 0.26,
                itc_utilization_factor: float = 1.0,
                itc_or_cash_grant_dollar:int = 0,
                fed_additional_grants:int= 10_000,
                fed_form: str = 'Performance'):
                self.itc_or_cash= itc_or_cash
                self.itc_amount= itc_amount
                self.itc_utilization_factor= itc_utilization_factor
                self.itc_or_cash_dollar = itc_or_cash_grant_dollar
                self.fed_additional_grants= fed_additional_grants
                self.fed_form = fed_form
class CostStateIncInputs:
        def __init__(self,
                itc_amount: float = 0.30,
                itc_utilization_factor: float = 1.0,
                itc_realization_period: int = 5,
                itc_or_cash_grant_dollar:int = 0,
                state_additional_grants:float= 0.0,
                state_form:str = 'Neither'):
                self.itc_amount= itc_amount
                self.itc_utilization_factor= itc_utilization_factor
                self.itc_realization_period= itc_realization_period
                self.itc_or_cash_dollar= itc_or_cash_grant_dollar
                self.state_additional_grants= state_additional_grants
                self.state_form = state_form
class CostFedIncInputsPerf:
        def __init__(self,
                ptc_or_repi: str = 'PTC',
                pbi_rate: float = 2.3,
                pbi_util_rate: float = 1.0,
                pbi_duration: int = 10,
                pbi_escalation_rate: float = 0.02,
        ):
                self.ptc_or_repi=  ptc_or_repi
                self.pbi_rate= pbi_rate
                self.pbi_util_rate= pbi_util_rate
                self.pbi_duration= pbi_duration
                self.pbi_escalation_rate= pbi_escalation_rate
                
class CostStateIncInputsPerf:
        def __init__(self,
                cash_or_taxit: str = 'Cash',
                pbi_cap: int = 0,
                pbi_rate: float = 1.5,
                pbi_util_rate: float = 1.0,
                pbi_duration: int = 10,
                pbi_escalation_rate: float = 0.02,
                total_cap = 500_000
        ):
                self.cash_or_taxit=  cash_or_taxit
                self.pbi_cap = pbi_cap
                self.pbi_rate= pbi_rate
                self.pbi_util_rate= pbi_util_rate
                self.pbi_duration= pbi_duration
                self.pbi_escalation_rate= pbi_escalation_rate
                self.total_cap = total_cap
class CapExInverterInputs:
        def __init__(self,
                first_replacement: int = 10,
                first_replacement_cost: float = 0.235,
                second_replacement: int = 20,
                second_replacement_cost: float = 0.245):
                self.first_replacement= first_replacement
                self.first_replacement_cost= first_replacement_cost
                self.second_replacement= second_replacement
                self.second_replacement_cost= second_replacement_cost

class ReservesInput:
        def __init__(self,
                fund_from_operations: bool = False,
                reserve_req: int = 100_000,
                debt_service_req: int = 6,
                om_wc_req: int = 6,
                interest_on_reserves: float = 0.02):
                self.fund_from_operations= fund_from_operations
                self.reserve_req= reserve_req
                self.debt_service_req= debt_service_req
                self.om_wc_req= om_wc_req
                self.interest_on_reserves= interest_on_reserves

class DepreciationInput:
        def __init__(self,
                bonus_depreciation: bool = True,
                bonus_depreciation_pc: float = 0.5):
                self.bonus_depreciation= bonus_depreciation
                self.bonus_depreciation_pc= bonus_depreciation_pc
from model import *
from numpy.testing import assert_equal, assert_array_equal, assert_array_almost_equal, assert_approx_equal, assert_allclose

model = Model()
model.find_coe()

def test_fixed_om():
    actual = model.fixed_om_expense()
    expected = np.array([-11000,-11176,-11355,-11536,-11721,-11909,-12099,-12293,-12489,-12689,-12892,-13099,-13308,-13521,-13737,-13957,-14181,-14407,-14638,-14872,-15110,-15352,-15597,-15847,-16101])
    assert_array_equal(actual,expected)

def test_var_om():
    actual = model.var_om_expense()
    expected = np.array([-348,-352,-355,-359,-363,-367,-371,-375,-379,-383,-388,-392,-396,-401,-405,-409,-414,-418,-423,-427,-432,-437,-442,-446,-451])
    assert_array_equal(actual,expected)

def test_insurance():
    actual = model.insurance()
    expected = np.array([-27500,-27940,-28387,-28841,-29303,-29772,-30248,-30732,-31224,-31723,-32231,-32746,-33270,-33803,-34344,-34893,-35451,-36019,-36595,-37180,-37775,-38380,-38994,-39618,-40251])
    assert_array_equal(actual,expected)

def test_project_management():
    actual = model.project_management()
    expected = np.array([-50000,-50800,-51613,-52439,-53278,-54130,-54996,-55876,-56770,-57678,-58601,-59539,-60492,-61459,-62443,-63442,-64457,-65488,-66536,-67601,-68682,-69781,-70898,-72032,-73184])
    assert_array_equal(actual,expected)

def test_property_taxes():
    actual = model.property_taxes()
    expected = np.array([-50000,-45000,-40500,-36450,-32805,-29525,-26572,-23915,-21523,-19371,-17434,-15691,-14121,-12709,-11438,-10295,-9265,-8339,-7505,-6754,-6079,-5471,-4924,-4431,-3988])
    assert_allclose(actual,expected,0.0005)

def test_land_lease():
    actual = model.land_lease()
    expected = np.array([-5000,-5080,-5161,-5244,-5328,-5413,-5500,-5588,-5677,-5768,-5860,-5954,-6049,-6146,-6244,-6344,-6446,-6549,-6654,-6760,-6868,-6978,-7090,-7203,-7318])
    assert_array_equal(actual,expected)

def test_production_degradation_factor():
    actual = model.production_degradation_factor()
    expected = np.array([1.00,0.995,0.990,0.985,0.980,0.975,0.970,0.966,0.961,0.956,0.951,0.946,0.942,0.937,0.932,0.928,0.923,0.918,0.914,0.909,0.905,0.900,0.896,0.891,0.887])
    assert_array_almost_equal(actual,expected,3)

def test_production():
    actual = model.production()
    expected = np.array([3477757,3460368,3443066,3425851,3408722,3391678,3374720,3357846,3341057,3324352,3307730,3291191,3274735,3258362,3242070,3225859,3209730,3193681,3177713,3161824,3146015,3130285,3114634,3099061,3083565])
    assert_array_almost_equal(actual,expected,0)

def test_tariff_rate_total():
    actual = model.tariff_rate_total()
    expected = np.array([27.85,28.41,28.98,29.55,30.15,30.75,31.36,31.99,32.63,33.28,33.95,34.63,35.32,36.03,36.75,37.48,38.23,39.00,39.78,40.57,0.00,0.00,0.00,0.00,0.00])
    assert_array_almost_equal(actual,expected,2)

def test_revenue_from_tariff():
    actual = model.revenue_from_tariff()
    expected = np.array([968555,982987,997633,1012498,1027584,1042895,1058434,1074205,1090211,1106455,1122941,1139673,1156654,1173888,1191379,1209131,1227147,1245431,1263988,1282821,0,0,0,0,0])
    assert_array_equal(actual,expected)

def test_market_revenue():
    actual = model.market_revenue()
    expected = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,284103,291163,298398,305813,313413])
    assert_array_equal(actual,expected)

def test_royalties():
    actual = model.royalties()
    expected = -np.array([29057,29490,29929,30375,30828,31287,31753,32226,32706,33194,33688,34190,34700,35217,35741,36274,36814,37363,37920,38485,8523,8735,8952,9174,9402])
    assert_array_equal(actual,expected)


def test_total_operating_expenses():
    actual = model.total_operating_expenses()
    expected = -np.array([172904,169837,167300,165244,163625,162402,161539,161005,160769,160807,161094,161610,162336,163256,164353,165614,167028,168583,170270,172079,143470,145133,146896,148752,150697])
    assert_allclose(actual,expected,0.00005)

def test_interest_on_reserves():
    actual = model.interest_on_reserves()
    expected = np.array([4647,5796,6944,8093,9242,10391,11540,12689,13838,9242,4671,5869,7067,8264,9462,10660,11858,13056,13025,7005,1615,1615,1615,1615,807])
    assert_array_equal(actual,expected)

def test_project_revenue_all():
    actual = model.project_revenue_all()
    expected = np.array([973202,988782,1004578,1020591,1036826,1053286,1069974,1086894,1104048,1115697,1127612,1145542,1163721,1182153,1200841,1219791,1239004,1258487,1277013,1289826,285717,292777,300013,307428,314220])
    assert_allclose(actual,expected,0.000005)

def test_ebitda():
    actual = model.ebitda()
    expected = np.array([800297,818945,837277,855347,873202,890885,908435,925889,943279,954890,966518,983931,1001384,1018897,1036489,1054177,1071977,1089904,1106743,1117747,142248,147644,153117,158676,163523])
    assert_allclose(actual,expected,0.00005)

def test_operating_income_after_interest_expense():
    actual = model.operating_income_after_interest_expense()
    expected = np.array([627252,650990,674768,698665,722754,747109,771798,796891,822454,842809,863794,891220,919386,948362,978219,1009031,1040874,1073826,1106743,1117747,142248,147644,153117,158676,163523])
    assert_allclose(actual,expected,0.00005)

def test_annual_conliq_reserves():
    actual = model.annual_conliq_reserves()
    expected = np.array([57444,57444,57444,57444,57444,57444,57444,57444,57444,-517000,59889,59889,59889,59889,59889,59889,59889,59889,-62989,-539000,0,0,0,0,-80732])
    assert_allclose(actual,expected,0.0005)

def test_adjustments_major_equipment():
    actual = model.adjustments_major_equipment()
    expected = -np.array([0,0,0,0,0,0,0,0,0,517000,0,0,0,0,0,0,0,0,0,539000,0,0,0,0,0])
    assert_array_equal(actual,expected)

def test_pretax_cash_flow_to_equity():
    actual = model.pretax_cash_flow_to_equity()
    expected = np.array([497098,515745,534077,552147,570002,587685,605235,622690,640079,709135,660874,678287,695740,713253,730844,748532,766332,784260,1169732,1117747,142248,147644,153117,158676,244255])
    assert_allclose(actual,expected,0.00005)

def test_net_pretax_cash_flow_to_equity():
    actual = model.net_pretax_cash_flow_to_equity()
    expected = np.array([-3368035,497098,515745,534077,552147,570002,587685,605235,622690,640079,709135,660874,678287,695740,713253,730844,748532,766332,784260,1169732,1117747,142248,147644,153117,158676,244255])
    assert_allclose(actual,expected,0.00005)

def test_annual_depreciation_expense():
    actual = model.annual_depreciation_expense()
    expected = np.array([3329579,662450,421805,276662,274583,165557,57530,57530,57557,160930,222997,156742,117063,117036,87284,32030,6583,6583,6583,114383,175771,103488,62093,62093,31046])
    assert_allclose(actual,expected,0.00005)

def test_taxable_income():
    actual = model.taxable_income()
    expected = np.array([-2702326,-11461,252963,422002,448171,581552,714268,739360,764896,681879,640797,734478,802323,831326,890935,977001,1034291,1067244,1100160,1003364,-33524,44156,91024,96583,132477])
    assert_allclose(actual,expected,0.005)

def test_after_tax_cash_flow_to_equity():
    actual = model.after_tax_cash_flow_to_equity()
    expected = np.array([-3368035,497098,515745,534077,552147,570002,587685,605235,584905,575063,651175,606406,423974,370598,376358,369793,352603,347186,351759,723892,711133,142248,143335,116229,119536,190569])
    assert_allclose(actual,expected,0.00005)


def test_as_generated_with_itc():
    model = Model()
    model.fincent_fed_form = 'Cost'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = True
    model.find_coe()
    actual = model.after_tax_cash_flow_to_equity()
    
    assert_equal(21.05, model.results_coe)

def test_as_generated_with_repi():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'REPI'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = True
    model.find_coe()
    actual = model.after_tax_cash_flow_to_equity()
    expected = np.array([-3366909,1569901,497972,408813,358040,364946,328228,291641,298567,305244,407572,322082,300353,289116,293661,285865,267424,260739,264024,634850,620765,155817,129736,116216,119522,189437])
    assert_allclose(actual,expected,0.00002)
    assert_equal(24.45, model.results_coe)

def test_as_generated_with_ptc():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.find_coe()
    actual = model.after_tax_cash_flow_to_equity()
    expected = np.array([-3365769,1577277,505689,416646,365990,373015,336417,299953,307003,313806,416261,291823,269643,257949,262030,253762,234844,227673,230466,600792,586200,155800,129723,116202,119509,188290])
    assert_allclose(actual,expected,0.00002)
    assert_equal(23.15, round(model.results_coe,2))

def test_as_generated_with_cash_with_state_cost():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Cost'
    model.find_coe()
    assert_equal(19.55, round(model.results_coe,2))

def test_as_generated_with_cash_with_state_cost_carry_forward():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = False
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Cost'
    model.find_coe()
    assert_equal(23.15, round(model.results_coe,2))

def test_fed_generated_performance_ptc_state_carried_performance_cash():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = False
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Cash'
    model.find_coe()
    assert_equal(22.55, round(model.results_coe,2))

def test_fed_generated_performance_ptc_state_carried_performance_taxcredit():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = False
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Tax Credit'
    model.find_coe()
    assert_equal(23.25, round(model.results_coe,2))

def test_fed_generated_performance_ptc_state_generated_performance_taxcredit():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Tax Credit'
    model.find_coe()
    assert_equal(21.15, round(model.results_coe,2))

def test_fed_generated_performance_ptc_state_generated_performance_taxcredit_additional_grant():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Tax Credit'
    model.fincent_state_additional_grants = 0.01
    model.refresh()
    model.find_coe()
    assert_equal(20.95, round(model.results_coe,2))

def test_fed_generated_performance_ptc_state_generated_performance_cash_additional_grant():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Cash'
    model.fincent_state_additional_grants = 0.01
    model.refresh()
    model.find_coe()
    assert_equal(21.85, round(model.results_coe,2))

def test_fed_generated_performance_ptc_state_generated_performance_cash_additional_grant_operations():
    model = Model()
    model.fincent_fed_form = 'Performance'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Cash'
    model.fincent_state_additional_grants = 0.01
    model.res_fund_from_operations = True
    model.refresh()
    model.find_coe()
    assert_equal(22.05, round(model.results_coe,2))


def test_fed_generated_neither_state_generated_performance_cash_additional_grant_operations():
    model = Model()
    model.fincent_fed_form = 'Neither'
    model.fed_ptc_or_repi = 'PTC'
    model.tax_fed_generated = True
    model.tax_state_generated = True
    model.fincent_fed_itc_or_cash = False
    model.fincent_state_form = 'Performance'
    model.state_cash_or_taxit = 'Cash'
    model.fincent_state_additional_grants = 0.01
    model.res_fund_from_operations = True
    model.refresh()
    model.find_coe()
    assert_equal(25.15, round(model.results_coe,2))
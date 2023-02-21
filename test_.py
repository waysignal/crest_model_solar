from model import *
from numpy.testing import assert_array_equal, assert_array_almost_equal, assert_approx_equal, assert_allclose

model = Model()

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
    expected = np.array([28.05,28.61,29.18,29.77,30.36,30.97,31.59,32.22,32.87,33.52,34.19,34.88,35.57,36.29,37.01,37.75,38.51,39.28,40.06,40.86,0.00,0.00,0.00,0.00,0.00])
    assert_array_almost_equal(actual,expected,2)

def test_revenue_from_tariff():
    actual = model.revenue_from_tariff()
    expected = np.array([975511,990046,1004798,1019769,1034964,1050385,1066035,1081919,1098040,1114401,1131005,1147857,1164960,1182318,1199935,1217814,1235959,1254375,1273065,1292034,0,0,0,0,0])
    assert_array_equal(actual,expected)

def test_market_revenue():
    actual = model.market_revenue()
    expected = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,284103,291163,298398,305813,313413])
    assert_array_equal(actual,expected)

def test_royalties():
    actual = model.royalties()
    expected = np.array([-29265,-29701,-30144,-30593,-31049,-31512,-31981,-32458,-32941,-33432,-33930,-34436,-34949,-35470,-35998,-36534,-37079,-37631,-38192,-38761,-8523,-8735,-8952,-9174,-9402])
    assert_array_equal(actual,expected)


def test_total_operating_expenses():
    actual = model.total_operating_expenses()
    expected = np.array([-173113,-170049,-167515,-165463,-163846,-162626,-161767,-161236,-161004,-161045,-161336,-161856,-162586,-163508,-164609,-165874,-167292,-168851,-170542,-172356,-143470,-145133,-146896,-148752,-150697])
    assert_allclose(actual,expected,0.00005)

def test_interest_on_reserves():
    actual = model.interest_on_reserves()
    expected = np.array([4651,5800,6949,8098,9247,10396,11545,12694,13843,9247,4676,5874,7071,8269,9467,10665,11863,13060,13028,7007,1617,1617,1617,1617,808])
    assert_array_equal(actual,expected)

def test_project_revenue_all():
    actual = model.project_revenue_all()
    expected = np.array([980162,995846,1011747,1027867,1044211,1060781,1077580,1094613,1111882,1123648,1135681,1153731,1172032,1190587,1209402,1228479,1247822,1267435,1286093,1299040,285719,292779,300015,307430,314221])
    assert_allclose(actual,expected,0.000005)

def test_ebitda():
    actual = model.ebitda()
    expected = np.array([807049,825797,844232,862405,880364,898154,915813,933377,950878,962602,974345,991875,1009446,1027079,1044793,1062604,1080530,1098584,1115551,1126685,142249,147646,153119,158678,163524])
    assert_allclose(actual,expected,0.00005)

def test_operating_income_after_interest_expense():
    actual = model.operating_income_after_interest_expense()
    expected = np.array([633799,657643,681530,705537,729739,754208,779014,804226,829910,850389,871500,899054,927351,956460,986454,1017405,1049390,1082488,1115551,1126685,142249,147646,153119,158678,163524])
    assert_allclose(actual,expected,0.00005)

def test_annual_conliq_reserves():
    actual = model.annual_conliq_reserves()
    expected = -np.array([-57444,-57444,-57444,-57444,-57444,-57444,-57444,-57444,-57444,517000,-59889,-59889,-59889,-59889,-59889,-59889,-59889,-59889,63134,539000,-0,-0,-0,-0,80828])
    assert_allclose(actual,expected,0.0005)

def test_adjustments_major_equipment():
    actual = model.adjustments_major_equipment()
    expected = -np.array([0,0,0,0,0,0,0,0,0,517000,0,0,0,0,0,0,0,0,0,539000,0,0,0,0,0])
    assert_array_equal(actual,expected)

def test_pretax_cash_flow_to_equity():
    actual = model.pretax_cash_flow_to_equity()
    expected = np.array([503559,522307,540741,558914,576874,594663,612322,629886,647388,716556,668410,685940,703511,721144,738857,756669,774595,792649,1178685,1126685,142249,147646,153119,158678,244352])
    assert_allclose(actual,expected,0.00005)

def test_net_pretax_cash_flow_to_equity():
    actual = model.net_pretax_cash_flow_to_equity()
    expected = np.array([-3371852,503559,522307,540741,558914,576874,594663,612322,629886,647388,716556,668410,685940,703511,721144,738857,756669,774595,792649,1178685,1126685,142249,147646,153119,158678,244352])
    assert_allclose(actual,expected,0.00005)

def test_annual_depreciation_expense():
    actual = model.annual_depreciation_expense()
    expected = np.array([3054298,607661,386920,253782,251875,151866,52775,52775,52799,156175,218239,151990,112310,112285,82530,29384,6041,6041,6041,113841,175500,103488,62093,62093,31046])
    assert_allclose(actual,expected,0.00005)

def test_taxable_income():
    actual = model.taxable_income()
    expected = np.array([-2420498,49982,294610,451755,477864,602342,726240,751451,777110,694215,653261,747064,815041,844176,903923,988021,1043349,1076447,1109510,1012844,-33251,44158,91026,96585,132478])
    assert_allclose(actual,expected,0.0005)

def test_taxable_income_with_carry_forward():
    actual = model.taxable_income_with_carry_forward()
    expected = np.array([0,0,0,0,0,0,182295,751451,777110,694215,653261,747064,815041,844176,903923,988021,1043349,1076447,1109510,1012844,0,10907,91026,96585,132478])
    assert_allclose(actual,expected,0.0005)

def test_after_tax_cash_flow_to_equity():
    actual = model.after_tax_cash_flow_to_equity()
    expected = np.array([-3371852,503559,522307,540741,558914,576874,594663,596827,566013,581333,657548,600652,383192,373216,379042,372542,356273,351778,356419,729056,716230,142249,143226,116230,119537,190666])
    assert_allclose(actual,expected,0.00005)
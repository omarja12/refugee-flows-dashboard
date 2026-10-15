"""Smoke check: the app serves its page and every callback builds its figures
for every year, segment and grouping the controls offer."""
import app as dashboard

client = dashboard.server.test_client()
assert client.get("/").status_code == 200
assert client.get("/_dash-layout").status_code == 200

for tab in ["tab-1", "tab-2", "tab-3"]:
    assert dashboard.show_content(tab) is not None, tab

years = sorted(int(y) for y in dashboard.demo["Year"].unique())
for year in years:
    for segment in ["Origin", "Asylum"]:
        choropleth, bar = dashboard.plots_1(year, 5, segment)
        assert choropleth and bar
        for level in ["Continent", "Region"]:
            options = dashboard.set_sub_choice_options(level)
            choice = dashboard.set_sub_choice_value(options)
            assert dashboard.plots_2(segment, level, choice, year)
    for group in ["By Gender", "By Age Group"]:
        sunburst, line = dashboard.plots_3(year, "Total", [years[0], years[-1]], group)
        assert sunburst and line

print(f"checked {len(years)} years, all callbacks returned figures")

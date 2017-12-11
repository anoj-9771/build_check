import pygal


def question(answer):
    if answer == "1":
        codeword = 'WAYSTATION VM'
    elif answer == "2":
        codeword = 'XPe STAGING'
    elif answer == "3":
        codeword = 'PRODUCTION VM'
    elif answer == "4":
        codeword = "POS0099:    PKG: "
    return codeword

def make_pie(answer, upgraded, pending):
    pie_chart = pygal.Pie()
    pie_chart.title = 'AU NP6 Builds'
    pie_chart.add('Upgraded', len(upgraded))
    pie_chart.add('Others', len(pending))
    if answer == "1":
        pie_chart.render_to_file('AU_Waystation_status.svg')
    elif answer == "2":
        pie_chart.render_to_file('AU_Staging_build_status.svg')
    elif answer == "3":
        pie_chart.render_to_file('AU_Production_status.svg')

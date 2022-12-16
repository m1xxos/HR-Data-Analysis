import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    def count_bigger_5(series):
        return sum(series > 5)

    office_a = pd.read_xml('../Data/A_office_data.xml')
    office_b = pd.read_xml('../Data/B_office_data.xml')
    hr_data = pd.read_xml('../Data/hr_data.xml')

    office_a.index = ['A' + str(a) for a in office_a['employee_office_id']]
    office_b.index = ['B' + str(b) for b in office_b['employee_office_id']]
    hr_data.set_index('employee_id', inplace=True)

    office_combine = pd.concat([office_a, office_b])
    office_merge = office_combine.merge(hr_data, left_index=True, right_index=True, indicator=True)

    office_merge.drop(['employee_office_id', '_merge'], axis=1, inplace=True)
    office_merge.sort_index(inplace=True)

    hard_working = office_merge.sort_values("average_monthly_hours", ascending=False)[:10]
    low_salary_projects = office_merge.query("Department == 'IT' & salary == 'low'")
    specific_employ = office_merge.loc[["A4", "B7064", "A3033"], ["last_evaluation", "satisfaction_level"]]

    aggregation = {
        "number_project": ["median", count_bigger_5],
        "time_spend_company": ["median", "mean"],
        "Work_accident": "mean",
        "last_evaluation": ["mean", "std"]
    }
    two_groups = office_merge.groupby('left').agg(aggregation).round(2)

    office_pivot = office_merge.pivot_table(columns=['left', 'salary'], index="Department",
                                            values="average_monthly_hours", aggfunc='median')

    print(office_pivot.loc[(office_pivot[0]['high'] < office_pivot[0]['low'])
                           | (office_pivot[1]['high'] > office_pivot[1]['low'])].round(2).to_dict())

    office_pivot_2 = office_merge.pivot_table(index='time_spend_company', columns='promotion_last_5years',
                                              values=['satisfaction_level', 'last_evaluation'],
                                              aggfunc=['max', 'mean', 'min'])
    print(office_pivot_2.loc[office_pivot_2['mean']["last_evaluation"][0]
                             > office_pivot_2['mean']["last_evaluation"][1]].round(2).to_dict())

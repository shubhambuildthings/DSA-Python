import pandas as pd

def find_employee(employee: pd.DataFrame) -> pd.DataFrame:
    merge_df = employee.merge(
        employee,
        left_on = 'managerId',
        right_on = 'id'
    )

    result_df = merge_df[
        merge_df['salary_x'] > merge_df['salary_y']
    ]

    return result_df[['name_x']].rename(
        columns={'name_x': 'Employee'}
    )
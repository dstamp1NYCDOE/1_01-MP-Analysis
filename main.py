import pandas as pd
import utils


def main(data):
    year = data['year']
    semester = data['semester']
    marking_period = data['MP']


    cr_1_01_df = pd.read_csv('data/1_01.csv')
    cr_1_01_df = cr_1_01_df[cr_1_01_df['Course'].str[0] != 'Z']

    teachers_df = pd.read_excel(
        'data/MasterSchedule.xlsx', sheet_name='Teachers').fillna('')
    
    cr_1_01_df = cr_1_01_df.merge(
        teachers_df,
        left_on='Teacher1',
        right_on='Teacher Name',
        how='left'
    ).fillna('')

    cr_3_07_df = pd.read_csv('data/3_07.csv')

    cr_1_01_df = cr_1_01_df.merge(
        cr_3_07_df,
        on='StudentID',
        how='left'
    ).fillna('')



    teachers_lst = pd.unique(cr_1_01_df[['Teacher1_y', 'Teacher2_y']].values.ravel('K'))
    teachers_lst.sort()
    teachers_lst = teachers_lst[1:]


    output_cols = ['StudentID', 
                   'LastName_x', 
                   'FirstName_x', 
                   'Course', 'Section', 'Period', 'Room', 'Teacher1_y', 'Teacher2_y', 
                   'Student DOE Email',
                   f"Mark{marking_period[-1]}",
                    ]






    writer = pd.ExcelWriter(f'output/{semester}{year}-{marking_period} - Grades Analysis By Teacher.xlsx')
    num_of_students_per_teacher_lst = []
    for teacher in teachers_lst:
        students_df = cr_1_01_df[
            (cr_1_01_df['Teacher1_y'] == teacher) |
            (cr_1_01_df['Teacher2_y'] == teacher)
            ]
        students_df = students_df.drop_duplicates(subset=['StudentID','Course'])
        students_df = students_df.sort_values(by=['Period','Course'])
        students_df = students_df[output_cols]
        
        students_df.to_excel(writer, sheet_name=teacher, index=False)
    
   


    for sheet in writer.sheets:
        worksheet = writer.sheets[sheet]
        worksheet.freeze_panes(1, 3)
        worksheet.autofit()


    
    writer.close()

    return True


if __name__ == "__main__":
    data = {
        'semester':'Fall',
        'year':'2023',
        'MP':'MP1',
    }
    main(data)

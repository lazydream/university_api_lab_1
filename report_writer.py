# -*- coding: utf-8 -*-
import os
import xlsxwriter
from app_config import REPORT_TYPES, STUDENT_REPORT, DEPARTAMENT_REPORT, INSTITUTE_REPORT


class ReportWriter:

    _report_type = 1

    def __init__(self, report_type=INSTITUTE_REPORT):
        if report_type not in REPORT_TYPES:
            raise RuntimeError('Неверный тип отчета')
        self._report_type = report_type

    def make_report(self, report_data):
        if self._report_type == STUDENT_REPORT:
            self._student_report(report_data)
        elif self._report_type == INSTITUTE_REPORT:
            self._institute_report(report_data)
        elif self._report_type == DEPARTAMENT_REPORT:
            pass

    def _student_report(self, report_dict):
        current_directory = os.path.curdir
        os.chdir(os.path.join(os.path.curdir, 'reports'))

        name = 'report_{report_type}'.format(report_type=self._report_type)
        workbook = xlsxwriter.Workbook(name + '.xlsx')
        worksheet = workbook.add_worksheet(name=name)
        bold = workbook.add_format({'bold': True})

        for heading in report_dict['headings']:
            worksheet.write(0, report_dict['headings'].index(heading), heading, bold)

        row = 1
        for entry in report_dict['report_data']:
            col = 0
            for k, v in entry.items():
                worksheet.write(row, col, v)
                col += 1
            row += 1
        workbook.close()
        os.chdir(current_directory)

    def _institute_report(self, report_dict):
        pass




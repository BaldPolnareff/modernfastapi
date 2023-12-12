from local_data.fake_db import fake_reports 

from models.report import WeatherReport

def get_reports(db: list[WeatherReport] = fake_reports.reports) -> list[WeatherReport]:
    return list(db) # return a copy of the list

def add_report(report: WeatherReport, db: list[WeatherReport] = fake_reports.reports) -> WeatherReport:
    db.append(report.model_dump())
    # let's sort the list by the report's dt field
    # db.sort(key=lambda r: r.dt)
    return db 
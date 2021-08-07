# Open Data of Taiwan's COVID-19 Vaccination Stats
 
We are making TW CDC's vaccination data ***completely accessible*** and ***easy to use***, as CDC currenlty only published [daily/weekly reports](https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og) as PDFs. 
 
## Stats by vaccine type, updated daily

Daily and cumulative stats for each type of vaccine in [`CSV`](data/tw_covid19_vaccinations_by_vaccine_type.csv) and [`JSON`](tw_covid19_vaccinations_by_vaccine_type.json), including each vaccine's 1st vs. 2nd shots. 

We use the common vaccines names used by Taiwanese in the data headers for these 5 vaccines:
1. AZ: Oxford/AstraZeneca
2. BNT: Pfizer-BioNTech 🤔
3. 莫德納: Moderna
4. 高端: Medigen (MVC-COV1901)
5. 聯亞: Vaxxinity/UBI (UBI-612)

Source: automatically extracted from the [daily PDF reports](https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og) published by Taiwan CDC.

## Vaccine arrival stats

Details for each vaccine shipment arrival and cumulative stats for: [AZ](data/tw.gov.fda.vaccine_arrival/vaccine_arrival_az.csv), [莫德納](data/tw.gov.fda.vaccine_arrival/vaccine_arrival_moderna.csv), [高端](data/tw.gov.fda.vaccine_arrival/vaccine_arrival_medigen.csv).

## Archive of Taiwan CDC's [vaccination reports](data/tw.gov.cdc.vaccination_reports): 

Thanks to g0v contributors, we have reports going back to March. If you have copies of any missing reports, please contribute via a pull request, thanks!

Source: [Daily, weekly, and adverse event reports](https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og) published by Taiwan CDC. 

## Other open data resources

* 國家高速網路與計算中心 (NCHC) provides many [charts on vaccination](https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php) and 2 APIs:
  * Daily updates on [vaccinations by city](https://covid-19.nchc.org.tw/api.php?tableID=2003) ([json](https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2003)): without data on vaccine type nor daily shots.
  * Weekly updates on [vaccinations and inventory by city](https://covid-19.nchc.org.tw/api.php?tableID=2001) ([json](https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2001)): without daily data nor data on 1st vs. 2nd shots.
* 天下雜誌 provides daily updates on [vaccinations by vaccine type](https://github.com/cwgrouptw/data) ([csv](https://github.com/cwgrouptw/data/blob/main/covid-19/taiwan-vaccinations.csv)): without data on 1st vs. 2nd shots by vaccine type. 


## Feedback

Drop by the #vaccine channel on [g0v's Slack](https://join.g0v.tw/).

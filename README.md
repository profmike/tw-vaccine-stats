# Open Data of Taiwan's COVID-19 Vaccination Stats
 
We are working on making TW CDC's vaccination data accessible, as it is only published by CDC as [daily PDF reports](https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og). 
 
## Daily stats by vaccine type in [`data`](data)

Daily and cumulative stats for each type of vaccine, including stats for each vaccine's 1st vs. 2nd shots. 

We use the common vaccines names used by Taiwanese in the data headers:
* AZ: Oxford/AstraZeneca
* BNT: Pfizer-BioNTech
* Moderna
* 高端: Medigen (MVC-COV1901)
* 聯亞: Vaxxinity/UBI (UBI-612)

Source: automatically extracted from the [daily PDF reports](https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og) published by Taiwan CDC.

## Other open data resources
* 國家高速網路與計算中心 (NCHC) provides many [charts on vaccination](https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php) and 2 APIs:
  * [Daily stats on total vaccination by city](https://covid-19.nchc.org.tw/api.php?tableID=2003) without data on vaccine type.
  * [Weekly stats on total vaccination and inventory by city](https://covid-19.nchc.org.tw/api.php?tableID=2001) without data on 1st vs. 2nd shots.
* 天下雜誌 provides [daily stats on total vaccination by vaccine type](https://github.com/cwgrouptw/data), without data on each vaccine's 1st vs. 2nd shots. 


## Archive of Taiwan CDC's vaccination reports in [`data/pdf`](data/pdf): 

Thanks to g0v contributors, we have reports going back to March. If you have copies of any missing reports, please contribute via a pull request, thanks!

Source: [Daily, weekly, and adverse event reports](https://www.cdc.gov.tw/Category/Page/9jFXNbCe-sFK9EImRRi2Og) published by Taiwan CDC. 



## Discuss

Drop by the #vaccine channel on [g0v's Slack](https://join.g0v.tw/).

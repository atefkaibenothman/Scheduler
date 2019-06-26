# Scheduler

### Overview
A web-scraper tool that makes it easier for students to monitor class sizes using https://www.reg.uci.edu/perl/WebSoc.

### Setup
1. pip install beautifulsoup4
2. pip install requests
3. pip install pandas

### To-Do
- [ ] Use requests to get a list of all the departments.

### Database
<pre>
{
    department_name : 
    {
        course_name : 
        {
            course_code: 
            {
                      type: str,
                       sec: str,
                     units: int,
                instructor: str,
                      time: str,
                     place: str,
                     final: str,
                       max: int,
                  enrolled: int,
                  waitlist: str,
                 requested: int,
                  reserved: int,
               restriction: str,
                    status: str,
            }
        }
    }
}

Example:

{
    'I&C SCI' : 
    {
        '6B' : 
        {
            35330 : 
            {
                      type: 'Lec',
                       sec: 'A',
                     units: 4,
                instructor: 'Gassko, I',
                      time: 'MWF 12:00-12:50pm',
                     place: 'SSLH 100',
                     final: 'Mon Dec 9 1:30-3:30pm',
                       max: 399,
                  enrolled: 0,
                  waitlist: 'n/a',
                 requested: 47,
                  reserved: 399,
               restriction: 'A and N',
                    status: 'NewOnly',
            },
            35341 : 
            {
                      type: 'Dis',
                       sec: '1',
                     units: 0,
                instructor: 'Staff',
                      time: 'MW 2:00-2:50pm',
                     place: 'SH 134',
                     final: '',
                       max: 97,
                  enrolled: 0,
                  waitlist: 'n/a',
                 requested: 4,
                  reserved: 97,
               restriction: 'A and N',
                    status: 'NewOnly',
            }
        }
    }
}
</pre>


# Scheduler

### To-Do
- [x] Get a list of all the departments from https://www.reg.uci.edu/perl/WebSoc and write the departments to a text file.
- [ ] Go through each department and gather relevant course information.

### Course Info
1. course code
2. course type (e.g. lec/dis/lab)
3. section
4. units
5. instructor
6. time
7. place
8. final date/time
9. max enrollment allowed
10. waitlist
11. requested
12. nor (slots reserved for new students)
13. restriction codes
14. status

### Department Info
1. deadlines

### Template

<pre>
{ department name: 
    { course name: 
        { code: 
            { type: str, 
              sec: str, 
              units: int,
              instructor: str,
              time: str,
              place: str,
              final: str,
              max: int,
              enr: int,
              wl: str,
              req: int,
              nor: int,
              rstr: str,
              status: str }
        }
    }
}

Example:

{ "I&C SCI": 
    { "6B": 
        { 35330: 
            { type: "Lec", 
              sec: "A", 
              units: 4,
              instructor: "GASSKO, I",
              time: "MWF 12:00-12:50pm",
              place: "SSLH 100",
              final: "Mon Dec 9 1:30-3:30pm",
              max: 399,
              enr: 0,
              wl: "n/a",
              req: 47,
              nor: 399,
              rstr: "A and "N,
              status: "NewOnly" }
        },
        { 35341:
            { type: "Dis", 
              sec: "1", 
              units: 0,
              instructor: "STAFF", "GASSKO, I",
              time: "MW 2:00-2:50pm",
              place: "SH 134",
              final: "",
              max: 97,
              enr: 0,
              wl: "n/a",
              req: 4,
              nor: 97,
              rstr: "A and N",
              status: "NewOnly" }
        }
    }
}

</pre>


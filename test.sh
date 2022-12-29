for i in $(cat requirements.txt); do python json_perf_meter/main.py $i; done

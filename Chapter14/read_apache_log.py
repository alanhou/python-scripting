def read_apache_log(logfile):
    with open(logfile) as f:
        # log_obj = f.read()
        # print(log_obj)
        for i in range(5):
            print(next(f))

if __name__ == '__main__':
    read_apache_log('access.log')

        #open db connection
        db = sqlite3.connect('pmdb')
        cursor = db.cursor()
        #db software

        cursor.execute('''INSERT INTO swsumtable(version)
                VALUES(?)''', (version,))


        cursor.execute('''INSERT INTO swtable(devicename, model, iosversion, uptime, confreg)
                VALUES(?,?,?,?,?)''', (devicename, model, iosversion, uptime, confreg,))

        #db hardware

        cursor.execute('''INSERT INTO hwsumtable(model)
                VALUES(?)''', (model,))
        count_sql = 0


        for card in list_card:
                cursor.execute('''INSERT INTO hwcardtable(devicename, model, card, sn, hwdscr)
                        VALUES(?,?,?,?,?)''', (devicename,model,card,list_serial_number[count_sql],list_hardware_description[count_sql],))    
                count_sql+=1

        #db process cpu and memory

        cursor.execute('''INSERT INTO cpusumtable(devicename, model, total, process, interrupt, topcpu, status)
                VALUES(?,?,?,?,?,?,?)''', (devicename, model, total, process, interrupt, topcpu, status,))
          

        cursor.execute('''INSERT INTO memsumtable(devicename, model, utils, topproc, status)
                VALUES(?,?,?,?,?)''', (devicename, model, utils, topproc, status,))

        #db environment

        count_sql = 0
        for psu in list_psu:
            cursor.execute('''INSERT INTO envtable(devicename, system, item, status)
                    VALUES(?,?,?,?)''', (devicename,'Power Supply',psu,list_psu_cond[count_sql],))
            count_sql+=1


        count_sql = 0
        for fan in list_fan:
            cursor.execute('''INSERT INTO envtable(devicename, system, item, status)
                    VALUES(?,?,?,?)''', (devicename,'Fan',fan,list_fan_cond_cp[count_sql],))
            count_sql+=1


        count_sql = 0
        for temp in list_temp:
            cursor.execute('''INSERT INTO envtable(devicename, system, item, status)
                    VALUES(?,?,?,?)''', (devicename,'Temperature',temp,list_temp_cond[count_sql],))
            count_sql+=1

       #LOG Checking

        cursor.execute('''INSERT INTO logtable(devicename, model, script)
                VALUES(?,?,?)''', (devicename, model,self.__class__.__name__,))

        db.commit()             
        db.close()
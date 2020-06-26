import re

from netoprmgr_dm.device_templates.cisco.cisco_None import cisco_None
from netoprmgr_dm.device_templates.cisco.cisco_1905 import cisco_1905
from netoprmgr_dm.device_templates.cisco.cisco_1921 import cisco_1921
from netoprmgr_dm.device_templates.cisco.cisco_1941 import cisco_1941
from netoprmgr_dm.device_templates.cisco.cisco_2801 import cisco_2801
from netoprmgr_dm.device_templates.cisco.cisco_2811 import cisco_2811
from netoprmgr_dm.device_templates.cisco.cisco_2821 import cisco_2821
from netoprmgr_dm.device_templates.cisco.cisco_2901 import cisco_2901
from netoprmgr_dm.device_templates.cisco.cisco_2911 import cisco_2911
from netoprmgr_dm.device_templates.cisco.cisco_C3750X import cisco_C3750X
from netoprmgr_dm.device_templates.cisco.cisco_C4500X import cisco_C4500X
from netoprmgr_dm.device_templates.cisco.cisco_C4506 import cisco_C4506
from netoprmgr_dm.device_templates.cisco.cisco_C4507R import cisco_C4507R
from netoprmgr_dm.device_templates.cisco.cisco_C4507RE import cisco_C4507RE
from netoprmgr_dm.device_templates.cisco.cisco_C4900M import cisco_C4900M
from netoprmgr_dm.device_templates.cisco.cisco_C6504 import cisco_C6504
from netoprmgr_dm.device_templates.cisco.cisco_C6506 import cisco_C6506
from netoprmgr_dm.device_templates.cisco.cisco_C2960 import cisco_C2960
from netoprmgr_dm.device_templates.cisco.cisco_C2960C import cisco_C2960C
from netoprmgr_dm.device_templates.cisco.cisco_C2960CX import cisco_C2960CX
from netoprmgr_dm.device_templates.cisco.cisco_C2960L import cisco_C2960L
from netoprmgr_dm.device_templates.cisco.cisco_C2960S import cisco_C2960S
from netoprmgr_dm.device_templates.cisco.cisco_C2960X import cisco_C2960X
from netoprmgr_dm.device_templates.cisco.cisco_C2960XR import cisco_C2960XR
from netoprmgr_dm.device_templates.cisco.cisco_C3560 import cisco_C3560
from netoprmgr_dm.device_templates.cisco.cisco_C3560C import cisco_C3560C
from netoprmgr_dm.device_templates.cisco.cisco_C3560CG import cisco_C3560CG
from netoprmgr_dm.device_templates.cisco.cisco_C3560CX import cisco_C3560CX
from netoprmgr_dm.device_templates.cisco.cisco_C3560G import cisco_C3560G
from netoprmgr_dm.device_templates.cisco.cisco_C3560V2 import cisco_C3560V2
from netoprmgr_dm.device_templates.cisco.cisco_C3560X import cisco_C3560X
from netoprmgr_dm.device_templates.cisco.cisco_C3650 import cisco_C3650
from netoprmgr_dm.device_templates.cisco.cisco_C3750 import cisco_C3750
from netoprmgr_dm.device_templates.cisco.cisco_C3750E import cisco_C3750E
from netoprmgr_dm.device_templates.cisco.cisco_C3750G import cisco_C3750G
from netoprmgr_dm.device_templates.cisco.cisco_C3750V2 import cisco_C3750V2
from netoprmgr_dm.device_templates.cisco.cisco_C3850P import cisco_C3850P
from netoprmgr_dm.device_templates.cisco.cisco_C3850S import cisco_C3850S
from netoprmgr_dm.device_templates.cisco.cisco_C3850T import cisco_C3850T
from netoprmgr_dm.device_templates.cisco.cisco_C3850TS import cisco_C3850TS
from netoprmgr_dm.device_templates.cisco.cisco_C3850XS_S import cisco_C3850XS_S
from netoprmgr_dm.device_templates.cisco.cisco_C3850XS import cisco_C3850XS
from netoprmgr_dm.device_templates.cisco.cisco_C6509 import cisco_C6509
from netoprmgr_dm.device_templates.cisco.cisco_C6513 import cisco_C6513
from netoprmgr_dm.device_templates.cisco.cisco_C6807 import cisco_C6807
from netoprmgr_dm.device_templates.cisco.cisco_C6880 import cisco_C6880
from netoprmgr_dm.device_templates.cisco.cisco_C9200L import cisco_C9200L
from netoprmgr_dm.device_templates.cisco.cisco_C9300 import cisco_C9300
from netoprmgr_dm.device_templates.cisco.cisco_C9500 import cisco_C9500
from netoprmgr_dm.device_templates.cisco.cisco_2921 import cisco_2921
from netoprmgr_dm.device_templates.cisco.cisco_2951 import cisco_2951
from netoprmgr_dm.device_templates.cisco.cisco_3825 import cisco_3825
from netoprmgr_dm.device_templates.cisco.cisco_3845 import cisco_3845
from netoprmgr_dm.device_templates.cisco.cisco_3925 import cisco_3925
from netoprmgr_dm.device_templates.cisco.cisco_3945 import cisco_3945
from netoprmgr_dm.device_templates.cisco.cisco_ASA5505 import cisco_ASA5505
from netoprmgr_dm.device_templates.cisco.cisco_ASA5508 import cisco_ASA5508
from netoprmgr_dm.device_templates.cisco.cisco_ASA5512 import cisco_ASA5512
from netoprmgr_dm.device_templates.cisco.cisco_ASA5515 import cisco_ASA5515
from netoprmgr_dm.device_templates.cisco.cisco_ASA5520 import cisco_ASA5520
from netoprmgr_dm.device_templates.cisco.cisco_ISR4451 import cisco_ISR4451
from netoprmgr_dm.device_templates.cisco.cisco_ISR4331 import cisco_ISR4331
from netoprmgr_dm.device_templates.cisco.cisco_ISR4351 import cisco_ISR4351
from netoprmgr_dm.device_templates.cisco.cisco_ISR4321 import cisco_ISR4321
from netoprmgr_dm.device_templates.cisco.cisco_ASR1002 import cisco_ASR1002
from netoprmgr_dm.device_templates.cisco.cisco_ASA5585 import cisco_ASA5585
from netoprmgr_dm.device_templates.cisco.cisco_ASR9010 import cisco_ASR9010
from netoprmgr_dm.device_templates.cisco.cisco_ASR902 import cisco_ASR902
from netoprmgr_dm.device_templates.cisco.cisco_ISR4431 import cisco_ISR4431
from netoprmgr_dm.device_templates.cisco.cisco_C3850S_S import cisco_C3850S_S
from netoprmgr_dm.device_templates.cisco.cisco_C3850T_S import cisco_C3850T_S
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C93180YC_EX import cisco_N9K_C93180YC_EX
from netoprmgr_dm.device_templates.cisco.cisco_N7K_C7009 import cisco_N7K_C7009
from netoprmgr_dm.device_templates.cisco.cisco_N7K_C7010 import cisco_N7K_C7010
from netoprmgr_dm.device_templates.cisco.cisco_WLC_2504 import cisco_WLC_2504
from netoprmgr_dm.device_templates.cisco.cisco_WLC_3504 import cisco_WLC_3504
from netoprmgr_dm.device_templates.cisco.cisco_WLC_5508 import cisco_WLC_5508
from netoprmgr_dm.device_templates.cisco.cisco_WLC_5520 import cisco_WLC_5520
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C9372PX import cisco_N9K_C9372PX
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C93108TC_EX import cisco_N9K_C93108TC_EX
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C93108TC_FX import cisco_N9K_C93108TC_FX
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C93180YC_EX import cisco_N9K_C93180YC_EX
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C9504 import cisco_N9K_C9504
from netoprmgr_dm.device_templates.cisco.cisco_N9K_C9508 import cisco_N9K_C9508
from netoprmgr_dm.device_templates.cisco.cisco_VG224 import cisco_VG224

class file_identification:
    def __init__(self,file):
        self.file=file

    def file_identification(self):
        #count_file = 1
        #for file in self.files:
        executing_print = ('Beginning Execution')
        try:
            #print('')
            #print('File '+str(count_file)+' of '+str(len(self.files)))
            #print('Processing File :')
            #print(file)
            if '__init__.py' in self.file:
                pass
            elif 'pmdb' in self.file:
                pass
            elif '.zip' in self.file:
                pass
            else:
                try:
                    read_file = open(self.file, 'r')
                    read_file_list = read_file.readlines()
                except:
                    try:
                        read_file = open(self.file, 'r', encoding='latin-1')
                        read_file_list = read_file.readlines()
                    except:
                        print('Error Codec!!!')
                        pass
            
                for i in read_file_list:
                    if re.findall('.*PID:.*C3750X',i):
                        print('Execute cisco_C3750X')
                        cisco_C3750X(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*DESCR:.*C4500X',i):
                        print('Execute cisco_C4500X')
                        cisco_C4500X(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C4506',i):
                        print('Execute cisco_C4506')
                        cisco_C4506(self.file)
                        xcek='disable'
                        break
                    elif re.findall('^PID:\s+\S+4507R[+]E',i):
                        print('Execute cisco_C4507RE')
                        cisco_C4507RE(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C4507R',i):
                        print('Execute cisco_C4507R')
                        cisco_C4507R(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*DESCR:.*C4900M',i):
                        print('Execute cisco_C4900M')
                        cisco_C4900M(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C6504',i):
                        print('Execute cisco_C6504')
                        cisco_C6504(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C6506',i):
                        print('Execute cisco_C6506')
                        cisco_C6506(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960CX',i):
                        print ('Executing with C2960CX')
                        cisco_C2960CX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960C',i):
                        print ('Executing with C2960C')
                        cisco_C2960C(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960L',i):
                        print ('Executing with C2960L')
                        cisco_C2960L(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960S',i):
                        print ('Executing with C2960S')
                        cisco_C2960S(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960XR',i):
                        print ('Executing with C2960XR')
                        cisco_C2960XR(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960X',i):
                        print ('Executing with C2960X')
                        cisco_C2960X(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+2960',i):
                        print ('Executing with C2960')
                        cisco_C2960(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560CG',i):
                        print ('Executing with C3560CG')
                        cisco_C3560CG(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560CX',i):
                        print ('Executing with C3560CX')
                        cisco_C3560CX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560C',i):
                        print ('Executing with C3560C')
                        cisco_C3560C(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560G',i):
                        print ('Executing with C3560G')
                        cisco_C3560G(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560V2',i):
                        print ('Executing with C3560V2')
                        cisco_C3560V2(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560X',i):
                        print ('Executing with C3560X')
                        cisco_C3560X(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3560',i):
                        print ('Executing with C3560')
                        cisco_C3560(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+C3650',i):
                        print ('Executing with C3650')
                        cisco_C3650(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3750E',i):
                        print ('Executing with C3750E')
                        cisco_C3750E(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3750G',i):
                        print ('Executing with C3750G')
                        cisco_C3750G(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3750V2',i):
                        print ('Executing with C3750V2')
                        cisco_C3750V2(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+P',i):
                        print ('Executing with C3850P')
                        cisco_C3850P(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+S-S',i):
                        print ('Executing with C3850S_S')
                        cisco_C3850S_S(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+S',i):
                        print ('Executing with C3850S')
                        cisco_C3850S(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+TS',i):
                        print ('Executing with C3850TS')
                        cisco_C3850TS(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+T-S',i):
                        print ('Executing with C3850T_S')
                        cisco_C3850T_S(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+T',i):
                        print ('Executing with C3850T')
                        cisco_C3850T(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+XS-S',i):
                        print ('Executing with C3850XS_S')
                        cisco_C3850XS_S(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+\S+3850-\d+XS',i):
                        print ('Executing with C3850XS')
                        cisco_C3850XS(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C6509',i):
                        print('Executing with C6509')
                        cisco_C6509(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C6513',i):
                        print('Executing with C6513')
                        cisco_C6513(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C6807',i):
                        print('Executing with C6807')
                        cisco_C6807(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C6880',i):
                        print('Executing with C6880')
                        cisco_C6880(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C9200L',i):
                        print('Executing with C9200L')
                        cisco_C9200L(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C9300',i):
                        print('Executing with C9300')
                        cisco_C9300(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*C9500',i):
                        print('Executing with C9500')
                        cisco_C9500(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*CISCO2921',i):
                        print('Executing with CISCO2921')
                        cisco_2921(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*CISCO2951',i):
                        print('Executing with CISCO2951')
                        cisco_2951(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*CISCO3825',i):
                        print('Executing with CISCO3825')
                        cisco_3825(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*CISCO3845',i):
                        print('Executing with CISCO3845')
                        cisco_3845(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*CISCO3925',i):
                        print('Executing with CISCO3925')
                        cisco_3925(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*CISCO3945',i):
                        print('Executing with CISCO3945')
                        cisco_3945(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASA5505',i):
                        print('Executing with ASA5505')
                        cisco_ASA5505(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASA5508',i):
                        print('Executing with ASA5508')
                        cisco_ASA5508(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO1905',i):
                        print('Executing with 1905')
                        cisco_1905(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO1921',i):
                        print('Executing with 1921')
                        cisco_1921(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO1941',i):
                        print('Executing with 1941')
                        cisco_1941(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO2801',i):
                        print('Executing with 2801')
                        cisco_2801(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO2811',i):
                        print('Executing with 2811')
                        cisco_2811(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO2821',i):
                        print('Executing with 2821')
                        cisco_2821(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO2901',i):
                        print('Executing with 2901')
                        cisco_2901(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+CISCO2911',i):
                        print('Executing with 2911')
                        cisco_2911(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASA5512',i):
                        print('Executing with ASA5512')
                        cisco_ASA5512(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASA5515',i):
                        print('Executing with ASA5515')
                        cisco_ASA5515(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASA5520',i):
                        print('Executing with ASA5520')
                        cisco_ASA5520(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ISR4451',i):
                        print('Executing with ISR4451')
                        cisco_ISR4451(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ISR4331',i):
                        print('Executing with ISR4331')
                        cisco_ISR4331(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ISR4351',i):
                        print('Executing with ISR4351')
                        cisco_ISR4351(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ISR4321',i):
                        print('Executing with ISR4321')
                        cisco_ISR4321(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASR1002',i):
                        print('Executing with ASR1002')
                        cisco_ASR1002(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASA5585',i):
                        print('Executing with ASA5585')
                        cisco_ASA5585(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*A9K-RSP440-TR',i):
                        print('Executing with ASR9010')
                        cisco_ASR9010(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ASR-902',i):
                        print('Executing with ASR902')
                        cisco_ASR902(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*ISR4431\S+',i):
                        print('Executing with ISR4431')
                        cisco_ISR4431(self.file)
                        xcek='disable'
                        break
                    elif re.findall('PID:\s+N9K-C93180YC-EX',i):
                        print('Executing with N9K-C93180YC-EX')
                        cisco_N9K_C93180YC_EX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('PID:\s+N9K-C93180YC-EX',i):
                        print('Executing with N9K-C93180YC-EX')
                        cisco_N9K_C93180YC_EX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('PID:\s+N9K-C93108TC-EX',i):
                        print('Executing with N9K-C93108TC-EX')
                        cisco_N9K_C93108TC_EX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('PID:\s+N9K-C93108TC-FX',i):
                        print('Executing with N9K-C93108TC-FX')
                        cisco_N9K_C93108TC_FX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('PID:\s+N9K-C9372PX',i):
                        print('Executing with N9K-C9372PX')
                        cisco_N9K_C9372PX(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+N9K-C9504',i):
                        print('Executing with N9K-C9504')
                        cisco_N9K_C9504(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:\s+N9K-C9508',i):
                        print('Executing with N9K-C9508')
                        cisco_N9K_C9508(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*N7K-C7009',i):
                        print('Executing with N7K-C7009')
                        cisco_N7K_C7009(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*N7K-C7010',i):
                        print('Executing with N7K-C7010')
                        cisco_N7K_C7010(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*AIR-CT2504',i):
                        print('Executing with AIR-CT2504')
                        cisco_WLC_2504(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*AIR-CT3504',i):
                        print('Executing with AIR-CT3504')
                        cisco_WLC_3504(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*AIR-CT5508',i):
                        print('Executing with AIR-CT5508')
                        cisco_WLC_5508(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*AIR-CT5520',i):
                        print('Executing with AIR-CT5520')
                        cisco_WLC_5520(self.file)
                        xcek='disable'
                        break
                    elif re.findall('.*PID:.*VG224',i):
                        print('Executing with VG224')
                        cisco_VG224(self.file)
                        xcek='disable'
                        break
                    else:
                        xcek='enable'
                    
                if xcek=='enable':
                    executing_print=('Executing None')
                    cisco_None(self.file)
                
        #except NameError:
            #raise
        except:
            pass
            #count_file+=1
        return executing_print
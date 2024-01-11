def cek_gejala_jika_fakta(fakta, gejala):
    return gejala in fakta

def cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule):
    status = []
    hasil = None
    for r in rule[0:len(rule)-1]:
        si = cek_gejala_jika_fakta(fakta, r)
        status.append(si)
        if si:
            hasil = rule[len(rule)-1]

    if False in status:
        return False
    return hasil

def cek_jika_penyakit_ada_di_fakta_baru(penyakits, fakta):
    for penyakit in penyakits:
        if penyakit in fakta:
            return True
    return False

def cek_gejala_jika_fakta_berdasarkan_rules(fakta, rules, penyakits):
    fakta_baru = fakta
    
    while(cek_jika_penyakit_ada_di_fakta_baru(penyakits, fakta) != True) :
        for rule in rules:
            gejala_berdasarkan_rule = cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule)
            if gejala_berdasarkan_rule != False:
                if gejala_berdasarkan_rule in fakta_baru:
                    continue
                fakta_baru.append(gejala_berdasarkan_rule)

    return fakta_baru

def cari_akibat_rule(rules):
    akibat = []
    for rule in rules:
        akibat.append(rule[len(rule)-1])

    return akibat

def cari_sebab_rule_yang_bukan_akibat(rules):
    sebab = []
    for rule in rules:
        for g in rule[0:len(rule)-1]:
            if g not in cari_akibat_rule(rules) and g not in sebab:
                sebab.append(g)
                
    return sebab

def cari_index_rule(gejala, rules):
    for i in range(len(rules)):
        if gejala == rules[i][len(rules[i])-1] :
            return i
        else:
            continue
    return -1

def cek_gejala_jika_fakta_berdasarkan_rule2(fakta, rule_item):
    return rule_item in fakta

def buat_rule(rules):
    index = 1
    for rule in rules:
        print('R' + str(index) + '.\tIF ' + str(rule[0:len(rule)-1]) + ' THEN ' + rule[len(rule)-1] + '\n')
        index += 1

def buat_pertanyaan(rules, fakta):
    index = 1
    for i in cari_sebab_rule_yang_bukan_akibat(rules):
        print(str(index) + '.\tAPAKAH ANDA MENGALAMI ' + i + ' PADA TUBUH ANDA ?\n')
        index += 1

def print_cek_gejala_jika_fakta_berdasarkan_rules(fakta, rules, penyakits):
    fakta_baru = fakta
    index = 0
    
    while(cek_jika_penyakit_ada_di_fakta_baru(penyakits, fakta) == False) :
        for rule in rules:
            if cek_jika_penyakit_ada_di_fakta_baru(penyakits, fakta) != False:
                return

            gejala = rule[len(rule)-1]
            
            print('---------------------------------------')
            print(str(index+1) + '. COCOKKAN FAKTA DENGAN RULE ' + str(cari_index_rule(gejala, rules)+1))
            print('---------------------------------------\n')
            print('FAKTA\t: ')
            print('\t' + str(fakta_baru) + '\n')
            print('RULE ' + str(cari_index_rule(gejala, rules) + 1) + '\t:')
            print('\tIF ' + str(rule[0:len(rule)-1]) + ' THEN ' + str(rule[len(rule)-1]) + '\n')

            print_keberadaan_gejala_pada_fakta(fakta, rule)
            
            if cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule) != False:
                print('\nSTATUS\t: ')
                print('\tJALAN\n')
                
                if cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule) in fakta_baru:
                    print('\nSTATUS\t: ')
                    print('\tSUDAH JALAN\n')
                    index += 1
                    continue
                
                fakta_baru.append(cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule))
                print('FAKTA BARU : ' + cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule) + '\n')

            else:
                print('\nSTATUS\t: ')
                print('\tTIDAK JALAN\n')
            
            index += 1

    return fakta_baru

def print_keberadaan_gejala_pada_fakta(fakta, rule):
    for i in range(len(rule)-1):
        if cek_gejala_jika_fakta_berdasarkan_rule2(fakta, rule[i]):
            print('\t' + rule[i] + ' : FAKTA')
        else:
            print('\t' + rule[i] + ' : TIDAK FAKTA')

def print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fakta, rules, penyakits):
    fakta_baru = fakta
    index = 0

    rule_jalan = []

    fakta_lain = []

    print('DARI KESELURUHAN PROSES FORWARD CHAINING DIATAS, DAPAT DILIHAT :\n')

    print('\tFAKTA\t: ', end='')
    print(str(fakta) + '\n')

    while(cek_jika_penyakit_ada_di_fakta_baru(penyakits, fakta) is not True) :
        for rule in rules:
            if cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule) != False:
                if cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule) in fakta_baru:
                    continue
                
                fakta_baru.append(cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule))
                
                gejala = rule[len(rule)-1]
                rule_jalan.append('RULE ' + str(cari_index_rule(gejala, rules)+1))

                fakta_lain.append(str(cek_gejala_jika_fakta_berdasarkan_rule(fakta, rule)))
            else:
                pass
            
            index += 1

    print('\tRULE YANG JALAN\t\tFAKTA BARU:\n')
    e = 1
    for i, j in zip(rule_jalan, fakta_lain):
        print('\t' + str(e) + '. ' + str(i) + '\t\t' + str(j) + '\n')
        e += 1

    return fakta_baru                

def demo_1():
    penyakit = [
        "P1",
        "P2",
        "P3",
        "P4"
    ]

    fakta_gejala = [
        "G4", 
        "G5",
        "G6",
        "G7",
        "G11",
        "G13",
        "G16",
        "G17"
    ]
    
    rules = [
        ["G1", "G2", "G3", "P1"],
        ["G4", "G2", "G1"],
        ["G5", "G6", "G2"],
        ["G7", "G3"],
        ["G8", "G9", "G10", "P2"],
        ["G11", "G12", "G8", "G9"],
        ["G9", "G13", "G14", "P3"],
        ["G9", "G15", "G3", "P4"],
        ["G16", "G17", "G15"]
    ]

    print('\n+----------------------------------------------------------------+')
    print('|                               RULE                             |')
    print('+----------------------------------------------------------------+\n')

    buat_rule(rules)

    print('\n+----------------------------------------------------------------+')
    print('|                       DAFTAR PERTANYAAN                        |')
    print('+----------------------------------------------------------------+\n')
    
    buat_pertanyaan(rules, fakta_gejala)

    print('\n+----------------------------------------------------------------+')
    print('|                     PROSES FORWARD CHAINING                    |')
    print('+----------------------------------------------------------------+\n')
    
    print_cek_gejala_jika_fakta_berdasarkan_rules(fakta_gejala, rules, penyakit)

    penyakit = [
        "P1",
        "P2",
        "P3",
        "P4"
    ]

    fakta_gejala = [
        "G4", 
        "G5",
        "G6",
        "G7",
        "G11",
        "G13",
        "G16",
        "G17"
    ]
    
    rules = [
        ["G1", "G2", "G3", "P1"],
        ["G4", "G2", "G1"],
        ["G5", "G6", "G2"],
        ["G7", "G3"],
        ["G8", "G9", "G10", "P2"],
        ["G11", "G12", "G8", "G9"],
        ["G9", "G13", "G14", "P3"],
        ["G9", "G15", "G3", "P4"],
        ["G16", "G17", "G15"]
    ]

    print('\n+----------------------------------------------------------------+')
    print('|               KESIMPULAN PROSES FORWARD CHAININ                |')
    print('+----------------------------------------------------------------+\n')

    print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fakta_gejala, rules, penyakit)


def demo_2():
    penyakit = ["P3", "P4", "P1", "P2"]
    
    fakta_gejala = ["G4", "G5", "G6", "G7", "G11", "G13", "G16", "G17"]
    
    rules = [
        ["G1", "G2", "G3", "P1"],
        ["G4", "G2", "G1"],
        ["G5", "G6", "G2"],
        ["G7", "G3"],
        ["G8", "G9", "G10", "P2"],
        ["G11", "G12", "G8", "G9"],
        ["G9", "G13", "G14", "P3"],
        ["G9", "G15", "G3", "P4"],
        ["G16", "G17", "G15"]
    ]

    print(cek_gejala_jika_fakta_berdasarkan_rules(fakta_gejala, rules, penyakit))


def demo_3():
    penyakit = ["P1", "P2", "P3"]
    fakta_gejala = ["G1", "G3", "G5"]
    rules = [
        ["G1", "G2", "G3", "P1"],
        ["G4", "G2"],
        ["G5", "G6", "G4"],
        ["G1", "G5", "G6"],
        ["G1", "G7", "P2"],
        ["G1", "G4", "G2", "P3"]
    ]

    print(cek_gejala_jika_fakta_berdasarkan_rules(fakta_gejala, rules, penyakit))

def demo_4():
    penyakit = ["P1", "P2", "P3"]
    fakta_gejala = ["G1", "G3", "G5"]
    rules = [
        ["G1", "G2", "G3", "P1"],
        ["G4", "G2"],
        ["G5", "G6", "G4"],
        ["G1", "G5", "G6"],
        ["G1", "G7", "P2"],
        ["G1", "G4", "G2", "P3"]
    ]

    print('\n+----------------------------------------------------------------+')
    print('|                               RULE                             |')
    print('+----------------------------------------------------------------+\n')

    buat_rule(rules)

    print('\n+----------------------------------------------------------------+')
    print('|                       DAFTAR PERTANYAAN                        |')
    print('+----------------------------------------------------------------+\n')
    
    buat_pertanyaan(rules, fakta_gejala)

    print('\n+----------------------------------------------------------------+')
    print('|                     PROSES FORWARD CHAINING                    |')
    print('+----------------------------------------------------------------+\n')
    
    print_cek_gejala_jika_fakta_berdasarkan_rules(fakta_gejala, rules, penyakit)

    print('\n+----------------------------------------------------------------+')
    print('|               KESIMPULAN PROSES FORWARD CHAININ                |')
    print('+----------------------------------------------------------------+\n')

    penyakit = ["P1", "P2", "P3"]
    fakta_gejala = ["G1", "G3", "G5"]
    rules = [
        ["G1", "G2", "G3", "P1"],
        ["G4", "G2"],
        ["G5", "G6", "G4"],
        ["G1", "G5", "G6"],
        ["G1", "G7", "P2"],
        ["G1", "G4", "G2", "P3"]
    ]

    print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fakta_gejala, rules, penyakit)

def demo_5():
    penyakit = ["P1", "P2"]
    fakta_gejala = ["G2", "G8", "G5", "G11", "G3", "G13", "G4"]
    rules = [
        ["G1", "G7", "G6", "G9", "P1"],
        ["G2", "G4", "G3", "G1"],
        ["G1", "G5", "G7"],
        ["G7", "G8", "G6"],
        ["G6", "G10", "G9"],
        ["G14", "G10"],
        ["G6", "G12", "G16", "G15", "P2"],
        ["G6", "G7", "G2", "G12"],
        ["G15", "G14", "G16"],
        ["G12", "G13", "G15"],
        ["G11", "G14"]
    ]

    print('\n+----------------------------------------------------------------+')
    print('|                               RULE                             |')
    print('+----------------------------------------------------------------+\n')

    buat_rule(rules)

    print('\n+----------------------------------------------------------------+')
    print('|                       DAFTAR PERTANYAAN                        |')
    print('+----------------------------------------------------------------+\n')
    
    buat_pertanyaan(rules, fakta_gejala)

    print('\n+----------------------------------------------------------------+')
    print('|                     PROSES FORWARD CHAINING                    |')
    print('+----------------------------------------------------------------+\n')
    
    print_cek_gejala_jika_fakta_berdasarkan_rules(fakta_gejala, rules, penyakit)

    print('\n+----------------------------------------------------------------+')
    print('|               KESIMPULAN PROSES FORWARD CHAININ                |')
    print('+----------------------------------------------------------------+\n')

    penyakit = ["P1", "P2"]

    fakta_gejala = ["G2", "G8", "G5", "G11", "G3", "G13", "G4"]
    
    rules = [
        ["G1", "G7", "G6", "G9", "P1"],
        ["G2", "G4", "G3", "G1"],
        ["G1", "G5", "G7"],
        ["G7", "G8", "G6"],
        ["G6", "G10", "G9"],
        ["G14", "G10"],
        ["G6", "G12", "G16", "G15", "P2"],
        ["G6", "G7", "G2", "G12"],
        ["G15", "G14", "G16"],
        ["G12", "G13", "G15"],
        ["G11", "G14"]
    ]

    print_cek_gejala_jika_fakta_berdasarkan_rules_kesimpulan(fakta_gejala, rules, penyakit)

if __name__ == '__main__':
    demo_5()
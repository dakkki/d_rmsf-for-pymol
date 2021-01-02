import sys

def get_d_rmsf(wtdata,mutdata):
    d_rmsf_list = []
    with open(wtdata,'r') as data_wt:
        with open(mutdata,'r') as data_mut:
            wt_str = data_wt.readlines()
            mut_str = data_mut.readlines()
            if len(wt_str) == len(mut_str):
                for i in range(len(wt_str))[1:]:
                    
                    wt_rmsf = float(wt_str[i][15:21])
                    mut_rmsf = float(mut_str[i][15:21])
                    d_rmsf_list.append('%.3f' % (mut_rmsf-wt_rmsf))
                    
            else:
                print('two dat files line nums not equal')
    return d_rmsf_list

def write2pdb(d_rmsf_list,refpdb,outpdb):
    with open(refpdb,'r') as pdb:
        pdb_str = pdb.readlines()
        with open(outpdb,'a+') as w_pdb:
            if len(d_rmsf_list) == int(pdb_str[-1][23:26])-155:
                for i in pdb_str:
                    res_num = int(i[23:26])
                    re_res_num = res_num - 156
                    w_pdb.write(i.replace(i[61:66],d_rmsf_list[re_res_num]))

            else:
                print('residue nums not equal')

def main(arglist):
	wtdata = arglist[0]
	mutdata= arglist[1]
	refpdb = arglist[2]
	outpdb = arglist[3]
	d_rmsf_list = get_d_rmsf(wtdata,mutdata)
	write2pdb(d_rmsf_list,refpdb,outpdb)

if __name__=='__main__':
    main(sys.argv[1:])

'''
test sample
python d_rmsf.py wtdata mutdata refpdb outpdb
'''
	

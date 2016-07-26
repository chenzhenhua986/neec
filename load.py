from pcb_dataset import PCBDataset

db = PCBDataset('/l/vision/v5/chen478/neec/cvl_pcb_dslr_8/')
pcb10 = db.pcb(144) # load specific PCB
image = pcb10.image() # PCB image
ics = pcb10.ics() # list of IC locations
print ics

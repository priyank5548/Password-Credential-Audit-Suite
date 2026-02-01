import sys
from impacket.examples.secretsdump import LocalOperations, SAMHashes

def parse_sam_hives(system_hive, sam_hive):
    print(f"[*] Parsing {sam_hive} using {system_hive}...")
    
    try:
        # LocalOperations manages the 'bootkey' extraction from the SYSTEM hive
        local_ops = LocalOperations(system_hive)
        bootkey = local_ops.getBootKey()
        
        # SAMHashes performs the decryption of the hashes in the SAM hive
        sam = SAMHashes(sam_hive, bootkey, isRemote=False)
        sam.dump()
        
        print("[+] Extraction complete.")
    except Exception as e:
        print(f"[!] Error parsing hives: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python sam_parser.py <SYSTEM_HIVE> <SAM_HIVE>")
    else:
        parse_sam_hives(sys.argv[1], sys.argv[2])

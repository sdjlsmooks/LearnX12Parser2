from x12_edi_tools.x12_parser import X12Parser


# Define a sample X12 850 message with SAC (Service, Promotion, Allowance, or Charge Information) loops
x12_message = """
ISA*00*          *00*          *ZZ*SENDERID       *ZZ*RECEIVERID     *230101*1200*U*00401*000000001*0*P*>~
GS*PO*SENDERID*RECEIVERID*20230701*1200*1*X*004010~
ST*850*0001~
BEG*00*SA*123456789**20230701~
REF*DP*042~
SAC*A*F050***1000*****02~
SAC*C*D240***50*****06~
N1*BT*BUYER NAME*92*12345~
N1*ST*SHIP TO NAME*92*67890~
PO1*1*10*EA*100.00**BP*789012345~
CTT*1~
SE*11*0001~
GE*1*1~
IEA*1*000000001~
"""

# Initialize the X12 parser
parser = X12Parser()

# Parse the X12 message

parsed_data = parser.parse(x12_message)
sacLoop=parsed_data['SAC']
# Function to extract SAC loops from parsed data
def extract_sac_loops(parsed_data):
    sac_loops = []
    for segment in parsed_data:
        if (segment.startswith('SAC')):
            sac_loops.append(segment)
        else:
            print(segment+" NOT SAC SEGMENT")
    return sac_loops


# Extract SAC loops
sac_loops = extract_sac_loops(parsed_data)

# Print SAC loop details
print("Extracted SAC Loops:")
for sac in sac_loops:
    print(sac.get('segment'))
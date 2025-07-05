from x12.schema.schema import Schema, Usage, by_segment, by_segment_element
from x12.parser.parse import parse

def schema() -> Schema:
    x12 = Schema('X12')
    isa = x12.add_child('ISA', Usage.REQUIRED, by_segment('ISA'))
    gs = isa.add_child('GS', Usage.REQUIRED, by_segment('GS'))
    st = gs.add_child('ST', Usage.REQUIRED, by_segment_element('ST', 1, ['850']))
    
    # Purchase Order Header
    beg = st.add_child('BEG', Usage.REQUIRED, by_segment('BEG'))
    
    # Reference Information
    st.add_child('REF', Usage.REQUIRED, by_segment('REF'))
    
    # Date/Time Reference
    st.add_child('DTM', Usage.REQUIRED, by_segment('DTM'))
    
    # Buyer Information Loop
    buyer = st.add_child('N1_BUYER', Usage.REQUIRED, by_segment_element('N1', 1, ['BY']))
    buyer.add_child('N3', Usage.REQUIRED, by_segment('N3'))
    buyer.add_child('N4', Usage.REQUIRED, by_segment('N4'))
    
    # Ship To Information Loop
    ship_to = st.add_child('N1_SHIPTO', Usage.REQUIRED, by_segment_element('N1', 1, ['ST']))
    ship_to.add_child('N3', Usage.REQUIRED, by_segment('N3'))
    ship_to.add_child('N4', Usage.REQUIRED, by_segment('N4'))
    
    # Line Item Detail
    detail = st.add_child('DETAIL', Usage.REQUIRED, by_segment('PO1'))
    detail.add_child('PID', Usage.REQUIRED, by_segment('PID'))
    
    # Summary
    st.add_child('TDS', Usage.REQUIRED, by_segment('TDS'))
    st.add_child('CTT', Usage.REQUIRED, by_segment('CTT'))
    
    # Transaction Set Trailer
    gs.add_child('SE', Usage.REQUIRED, by_segment('SE'))
    isa.add_child('GE', Usage.REQUIRED, by_segment('GE'))
    x12.add_child('IEA', Usage.REQUIRED, by_segment('IEA'))

    return x12


testschema = schema()
print(str(testschema))
loop = parse("d:\\personal\\LearnPython\\X12Parser\\test2.x12",testschema)
print("FULL LOOP BEFORE MODS")
print(str(loop))
isa = loop.loops[0].segments[0]
print(str(isa))
# Here's how you modify the different elements of a segment
isa.elements[0] = "DAVID"
print(str(isa))
print("FULL LOOP AFTER MODS")
print(str(loop))
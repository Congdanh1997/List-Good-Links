AT Command of SIM Bank：
1. AT+CWSIM
Check if the sim bank standby, return SWSIM OK

1. AT+NEXT00
All channels are reset and all channels are connected to the first SIM card. Return SWSIM OK.

1. AT+SWIT00-0013
Example: All channels switch to the 13th SIM card and return SWITCH OK.
Note that cannot omit “00”. The previous 00 represents all card responses, 0013 cannot be written 13 and the range can be 0000-0016. If it is 0000, all SIM cards are disconnected. If more than 0016, it is always maintained to keep 16th SIM card.

1. AT+USIM
Return the location of SIM card 

Examples:
1. AT+SWIT07-0003
The 7th channel l switch to the 3rd SIM card, return SWITCH OK.
 Note that cannot omit “00”. 0003 can not be written as 3,07 also; range can be 0000-0016, if it is 0000, the road SIM The card is disconnected. If it is greater than 0016, the way will always remain on the 16th SIM card.
print("""JRay's Exam score Calculator
this program is open source on
https://github.com/jray9487\n""")
# MNS = Minor subject; MJS = Major subject
# conf = configure
# Final Exam = FE
# National Defense = ND
# Weighted grades = WG

#MNS_conf (地+國防 or公+歷)
print("副科是什麼呢?(0=地理+國防 & 1=公民+歷史)")
mns_conf = int(input())
while mns_conf != 0 or 1:
    if mns_conf == 0:
        break
    if mns_conf == 1:
        break
    else:
      print("請輸入 0 或 1 (0=地理+國防 & 1=公民+歷史)")
      print("副科是什麼呢? (0=地理+國防 & 1=公民+歷史)")
      mns_conf = int(input())

#Bio_conf
print("有加選生物嗎?(0=沒有 & 1=有)")
bio_conf = int(input())
while bio_conf != 0 or 1:
     if bio_conf == 0:
        break
     if bio_conf == 1:
        break
     else:
      print("請輸入 0 或 1 (0=沒有 & 1=有)")
      print("有加選生物嗎? (0=沒有 & 1=有)")
      bio_conf = int(input())
    
#FE_conf(+PE and ND)
print("Do the score from the final Exam?(0=false,1=true)")
FE_conf = int(input())
while FE_conf != 0 or 1:
    if FE_conf == 0:
        break
    if FE_conf == 1:
        break
    else:
      print("請輸入 0 或 1 (0=不是 & 1=是)")
      print("是期末考嗎? (0=不是 & 1=是)")
      FE_conf = int(input())

#MJS_score_ input 
print("請輸入中文（4學分）成績")
Chi = int(input())
print("請輸入英文（4學分）成績")
Eng = int(input()) 
print("請輸入數學（4學分）成績")
Math = int(input())
print("請輸入物理（2學分）成績")
Phy = int(input())
print("請輸入化學（2學分）成績")
Che = int(input())

#Bio_Score_input
if bio_conf == 1:
    print("請輸入生物（2學分）成績")
    Bio = int(input())

#MNS_Score_input
if mns_conf == 1:                          #MNS_1
    print("請輸入公民（2學分）成績")
    Civ = int(input())
    print("請輸入歷史（2學分）成績")
    His = int(input())
    if FE_conf == 1:                       #MNS_1_FE
        print("請輸入體育（2學分）成績")
        PE = int(input())
elif mns_conf == 0:                        #MNS_0
    print("請輸入地理（2學分）成績")
    Geo = int(input())
    if FE_conf == 1:                       #MNS_0_FE
        print("請輸入國防（2學分）成績")
        ND = int(input())
        print("請輸入體育（2學分）成績")
        PE = int(input())

#MJS_Score_ouput
print("中文 :",Chi)
print("數學 :",Math)
print("英文 :",Eng)
print("物理 :",Phy)
print("化學 :",Che)

#Bio_Score_output
if bio_conf == 1:
    print("生物 :", Bio)

#MNS_Score_output
if mns_conf == 0:
    print("地理 :",Geo)
elif mns_conf == 1:
    print("公民 :",Civ)
    print("歷史 :",His)
    
#FE_Score_output
if FE_conf == 1:
    print("體育 :",PE)
    print("國防 :",ND)

#WG
if FE_conf == 0:
    if mns_conf == 0:
        if bio_conf == 0:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Geo))/18
        if bio_conf == 1:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Geo+Bio))/20
    if mns_conf == 1:
        if bio_conf == 0:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Civ+His))/20
        if bio_conf == 1:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Civ+His+Bio))/22
if FE_conf == 1:
    if mns_conf == 0:
        if bio_conf == 0:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Geo+PE+ND))/22
        if bio_conf == 1:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Geo+PE+ND+Bio))/24
    if mns_conf == 1:
        if bio_conf == 0:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Civ+His+PE))/22
        if bio_conf == 1:
            wg =( 4*(Chi+Math+Eng)+2*(Phy+Che+Civ+His+PE+Bio))/24
print("加權平均 :",wg)

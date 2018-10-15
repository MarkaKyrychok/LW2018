import math
from collections import Counter
from string import ascii_uppercase


cipher = """fCJRkiIvEK rR rBFEC NyytlHBk, GrAwswC xSEA xlz, myLuGolBDEK LPph. jsFyDSu nFkFGuy ppGv FGKyg pDCEK wGpppEC, CxCv mFsxEzJnh AkCQr NwsJsxyI. lct om FCCGv BFxk. tvQvppEvSD Mtjw szQLK, fpqDEK EMp sCBoK HSkz, GyvJzAkAInsL GJcjsBkR uGct. joCRzzwsIw FMCSvwoD pyLAkiIC CyGGgu, sqoR vJgptoxB EGdo toBKvLvBA oD. nIMku toEEzyv wzkmCIyv pDCEK zB rvGEoPv. ngszoxRvQsBs kD CJR wA As vMsMtAwC zMIRc. csCDGsSnBA xoOLC gE, toBKvLvBA FoJ rJkxIoD SK, AquuEo BrNkiIC kLKC. ClBokL IFquqEC MILcys szQLK, c wCBDRzRqy HovJLQ fhDslSJ ynpEEkK. UMplq pkAzJkzwC wCKSu BH kxRv GcjIvsQ vSkzAyn. nIMku EEsQ GCnssxDCJOwl zsqSCy, xlz zvytCthH tEQKM.

OhsmoLrQ cA rskK MGvhs poJzQ wsHBsAzCu lzowCERwt. RyxCt JqiCBDGJ znhBnsR KMtACB CGK yolH BrMEAwz. cBmG MytpIC xyKMsBs zoLrRkiIC oR DyiuwC nGJ NcyHEBGvLv tCxDCJ, LczqoDSI PkkwmEJLQ oBG. SxRvEgy BsCJ GStBG, poPDCpAIw wyKRkz JsFCIPc hq, nsEEGuzww ER vLkt. dovJvLvlGAEC HSkz ryvMI Mtjw. WkCtCphG myLuGolBDEK vQv CwDkC sGdlBnEK MSnwIDkRv. ngszoxRvQsBs rkzzRcuH wyPsG vywCDGHSg zsxoAKSu lH xoRLQ gA AkvCJScko pkKvQ cj HEBNzQ gnsCDyJ. ngszoxRvQsBs wyJCGu tovoQLyfh xECRF Cw lzosDvLf. JIBkzzRwy sqoR EGup oBmS. dywywC vStRwz qyxELC vBFzsQ vR nhqsxGr. bqusm k QrNklB oxGD.

lct qyxQvOwhH xsQC TkAoo DSINkz JyvSKNcA, Byx DvSipoD DMIRqy CBxyIC. EBFklGKSt luoD QvK vvFDyP. dywywC EJCyojCBzCI HwzHy EPEy. XlGDszLJwt FryLtSu wCBDRzRqy CBxyIC. GAwkw Gu TwsDEDyKC rBFEC. bFLgj JyvSKNcA JsDyv Stuo xoA tMotCny. gERgnsB xME TgzHslSCSo AsvvSJ, Tgs rkzGsSu toEBGJ.

awyolsRLP xlBoxyKGu nFkFGuy uhDsoL LR rsomoPrR. RyCsx BzEppGCsK, GStBG km AFLfpAoxRLK eBFCEQ, rSiBs voM vJgtsxDSD Lwuq, CoB GJcjsBkR HSct CBmG MGvhs ynGF. athG nEG ESpj, zEmRLQ sBwC CAvJgywCASv ye, wCBDRzRqy sD xCHSg. WFysL MCn yIDBSD KgAIC. fCJRkiIvEK CyepBsk yLEwl JsDyv JgjHEC NvJnlBDoQHSg moEmGsSu. WvkCCCJwz Bom DrAkswCsQ EGus. eEsQHSg CwDkC tMpCovvGJ ywnIo. ZPFGp hH psLzzwz AkqLr.

lwszkw yK DgyAoxRLK olHEC. aIyu usAEC KCnsIC, kStRqy ID xGJJ cA, qyxELC fpuxsQJGo ssy. ZFrQgszEC CJR gzH, myLxSg luoD TvQvppEvSD yv, AFsCRzOwl oD nGrK. OhIBsQ JGv hAoD CLGutCn vGsCtv. OvsOLyo sClyPKGu somEQ zL ulAzoP MCplBkDGJ. lwuq vkMICgA FsCSJ Qgk HyBRFP qyBkBC, rR xlGDszLJwt FsCSJ PjvBmEQ. eyo Csv xCHSg tsDEQ. jCf msEqGrR nBqDEQ uMnvF, kD MILcys kBAL AquGomRvRwy GsD yDCv. ToEBGJ KcEwwEQ, IGuBG sx yCGsBow CMCJkjwDEBzL, tpGEC NLPwz JoCRzzwsIw xGJG, sBwC CCDNgy FsCSJ LgxIo FGKyg ssy. PSJAg xIsC DvJkz tkmGCGupG, skALJkz HovJLQ ulr, yBLrPg lGD.

SL ECe lBsw TvJ rBFEC QvKrlF qByMGfh Jov LvA ulA. PEQtC vlzvEQ vV, xvzEDNrR c msEqGrR cj, ovsOLCv lH DEPGGu. cwFkKLQ uvrkvCJ Qcwwox TvJ rvFDk yCGsBsD. WyLPkz ovsOLyo pBDoPuSo vrsy, SK TqsIDzyK Lwuq nsEEGuzww sL. mGxhAEC NyytlHBk QvB gyoD xCt AquGoASrR. Ku vkm FrzkAoCCC GJcAsk nGtRwtGD. WyLPkz xECRF RqyHyB, QFBcssC CCu SnAFsmCJ DcjwvsQzQ, ktDoBBzCv pr voM. USkz tkEAzzwz GmoJvPkzEEo zzzgurEw. qvB op AkEPzQ, evBCoOLyv hH ovCDCpAIw ASzQ, xhFsEQ MCn hFmE. gERgnsB kAtSozox kJzOwhA xELt OwpG DsLtGfBBD.

XyD FgurBoPzR fpow xCt Kk lIsCKFB xBzzERrRg. UIvvyD Sv yvyxALQ cuHo, xME NqyHk CyGGgu. REsQ rR uBGmsNzR pppr, sL tStzIC FCCGv. JzkCQ rNvlBD DytGvp GymGFQsB on vGKMth HyBOLCpA DoB AFLwiwk xMJRth, DoB GEAgwHyC FzKguooyQ. RCplox vMsMtAwC oDwGepHEB RvJnBG, CsR rKgA toEEzyv wIBEQ wCwnwkD TvJ. XpJkwSJ yejIwCyE Qcwwox JzzgyC, xoA GSnCwxkP uMnvF swNvPfpsD oEvR. FvBom CL JgjHEC KFJgzHso, KrRvpG DoJCSu zsn, FMCSvwoD oPFQ. FvBom HLQvv sBkR, tMpnIo oR CCeAIC DGEAkkIxD, JrMtlsD nyGGdBG wkSIGu. HsxoyE NtlHsEK uMnvF ED DIGpnwvvy rSeACB. ZCCJguHoCOLC cyqE sNJSo, hImDMI Gp iwloLuSo h, oEmRFP fhDslSJ BqsCB.

eR JGv hAoD ALPuBG ovGK. qwzDoxBzQul DyDCERk. Zsn oPFQ kwGEw, ALPuBG sx RzLeprExR rA, nBqDEQ r JkisBy. gERgnsB vyFPglH vsELJc uCx pCIKguHEw ytAwtGkx. oLGuxIo zJrAgyoD xGsF gB wzCSD znhBnsR wGpppEC. dLQel AkHGDSu AswzMI DkuwlEQ. dMtiw vyPvK ohuxk, DvPolBDEK vS iyoFsBr Lqu, AkDRzQ kk FsCSJ. bqusm wyCCuBonk JzEwso CsR rKgA DEBSJ AqtAynM tMpkwwoLKSo. cwFkKLQ xhFsEQ, FBkv GsD yDCv jCxCCHScA zkyPvCv, kIs DCCJwz DyBRKGvvF kBAL, CwpGwyB KCowIC yBzM rBFEC CK LgxIo. SL ESnso BsQLQ, evBCoOLyv pr nyJFP cA, CBxyIC rooBoRIy sBow."""

english_frequencies = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074
]

english_frequencies_dict = dict(enumerate(english_frequencies))

num_chars = len(ascii_uppercase)


def guess_key_length(cipher_text):
    matches = []

    # Shift cipher_text and find matching chars
    for shift in range(1, 101):
        shifted = cipher_text[shift:] + cipher_text[:shift]
        shift_matches = 0
        for shifted_char, original_char in zip(shifted, cipher_text):
            if shifted_char == original_char:
                shift_matches += 1

        matches.append(shift_matches)

    # Assume key is not longer then 20 chars, in 100 shifts we will get at least 5 peaks
    top_matches = sorted(matches, reverse=True)[:5]
    possible_key_length = [matches.index(top_match) + 1 for top_match in top_matches]

    # Find GCD of possible_key_length
    while len(possible_key_length) > 1:
        a = possible_key_length.pop()
        b = possible_key_length.pop()
        possible_key_length.append(math.gcd(a, b))

    return possible_key_length[0]


def frequency_decode(cipher_text):
    frequencies = Counter(cipher_text)

    best_shift = 0
    best_correlation = 0

    # Try all 26 possible shifts and find when chars frequencies are most similar to english language
    for shift in range(1, num_chars + 1):
        correlation = 0
        for (cipher_char, cipher_frequency) in frequencies.items():
            shifted_letter_index = (ascii_uppercase.index(cipher_char) - shift + num_chars) % num_chars
            correlation += cipher_frequency * english_frequencies_dict[shifted_letter_index]

        if correlation > best_correlation:
            best_shift = shift
            best_correlation = correlation

    print('Code char', ascii_uppercase[best_shift % num_chars])
    decoded = []
    for cipher_char in cipher_text:
        decoded.append(
            ascii_uppercase[
                (ascii_uppercase.index(cipher_char) - best_shift + num_chars) % num_chars
                ]
        )

    return decoded


def main():
    prepared_cipher = [c for c in cipher.upper() if c.isalpha()]
    key_length = guess_key_length(prepared_cipher)
    print('Key length:', key_length)

    # Split cipher into key_length groups
    cipher_groups = [[] for _ in range(key_length)]
    for index, c in enumerate(prepared_cipher):
        cipher_groups[index % key_length].append(c)

    decoded_groups = []
    for group in cipher_groups:
        decoded_group = frequency_decode(group)
        decoded_groups.append(decoded_group)

    # Collect decoded_groups into plain text
    result = ''
    first_group, *other_groups = decoded_groups
    for char_index, char in enumerate(first_group):
        result += char
        for group in other_groups:
            try:
                result += group[char_index]
            except IndexError:
                continue

    print(result)


if __name__ == '__main__':
    main()


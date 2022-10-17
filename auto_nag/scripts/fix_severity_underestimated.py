# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from auto_nag.bzcleaner import BzCleaner

AFFECTED_BUG_IDS = [
    "1737489",
    "1631323",
    "1628122",
    "1616260",
    "1615282",
    "1613280",
    "1609672",
    "1605556",
    "1603956",
    "1601558",
    "1595743",
    "1586929",
    "1584855",
    "1579451",
    "1576130",
    "1575437",
    "1572995",
    "1572932",
    "1570722",
    "1568313",
    "1567639",
    "1566039",
    "1561974",
    "1561971",
    "1561850",
    "1561386",
    "1560834",
    "1560702",
    "1556212",
    "1554399",
    "1552456",
    "1550454",
    "1549204",
    "1545367",
    "1544413",
    "1543726",
    "1543354",
    "1543036",
    "1541072",
    "1537704",
    "1536480",
    "1536148",
    "1529591",
    "1529575",
    "1526983",
    "1526688",
    "1526207",
    "1522188",
    "1520942",
    "1520157",
    "1519268",
    "1515318",
    "1515061",
    "1511756",
    "1507582",
    "1506017",
    "1505960",
    "1505775",
    "1503662",
    "1502814",
    "1502610",
    "1499027",
    "1498093",
    "1495295",
    "1494772",
    "1493472",
    "1489904",
    "1489635",
    "1485683",
    "1484928",
    "1484185",
    "1481876",
    "1480452",
    "1479858",
    "1477594",
    "1476440",
    "1475831",
    "1473789",
    "1472415",
    "1471918",
    "1470829",
    "1470690",
    "1467469",
    "1467463",
    "1467338",
    "1467057",
    "1466440",
    "1465828",
    "1464685",
    "1464087",
    "1463546",
    "1460768",
    "1458894",
    "1455296",
    "1455154",
    "1453699",
    "1450600",
    "1450384",
    "1449956",
    "1449939",
    "1449139",
    "1448975",
    "1447524",
    "1446442",
    "1446265",
    "1445644",
    "1445547",
    "1445211",
    "1444567",
    "1440408",
    "1439905",
    "1438248",
    "1437524",
    "1433679",
    "1429838",
    "1428454",
    "1426058",
    "1424761",
    "1422891",
    "1422507",
    "1421289",
    "1421254",
    "1421021",
    "1419151",
    "1415267",
    "1413602",
    "1412634",
    "1411795",
    "1411693",
    "1411641",
    "1410932",
    "1410437",
    "1410302",
    "1409262",
    "1407972",
    "1407238",
    "1406996",
    "1406264",
    "1405971",
    "1405282",
    "1404560",
    "1404468",
    "1403823",
    "1403737",
    "1403498",
    "1403483",
    "1401793",
    "1401665",
    "1401091",
    "1399937",
    "1399147",
    "1398639",
    "1398528",
    "1398414",
    "1397242",
    "1395510",
    "1394448",
    "1393512",
    "1393248",
    "1392762",
    "1391805",
    "1391627",
    "1389040",
    "1388376",
    "1388154",
    "1385698",
    "1382018",
    "1379502",
    "1376061",
    "1374515",
    "1374505",
    "1374327",
    "1374004",
    "1368426",
    "1366211",
    "1364404",
    "1364261",
    "1361053",
    "1359861",
    "1356879",
    "1352769",
    "1352205",
    "1347761",
    "1346657",
    "1344657",
    "1335668",
    "1334918",
    "1333781",
    "1333395",
    "1333362",
    "1332714",
    "1332290",
    "1331920",
    "1330930",
    "1329884",
    "1328975",
    "1328776",
    "1327957",
    "1327812",
    "1327592",
    "1327572",
    "1327534",
    "1327035",
    "1326181",
    "1325692",
    "1324919",
    "1321850",
    "1321406",
    "1320757",
    "1320332",
    "1319080",
    "1317378",
    "1317166",
    "1315558",
    "1315471",
    "1315310",
    "1310551",
    "1310037",
    "1308059",
    "1307759",
    "1303739",
    "1303278",
    "1300411",
    "1297353",
    "1297029",
    "1296922",
    "1295122",
    "1293420",
    "1292701",
    "1289864",
    "1289491",
    "1286869",
    "1282984",
    "1279894",
    "1278699",
    "1278414",
    "1276449",
    "1273708",
    "1269810",
    "1269142",
    "1268395",
    "1267667",
    "1267145",
    "1266960",
    "1266837",
    "1265654",
    "1265457",
    "1263100",
    "1262128",
    "1260254",
    "1259924",
    "1259818",
    "1258112",
    "1255507",
    "1253484",
    "1251617",
    "1248768",
    "1247245",
    "1245502",
    "1245239",
    "1240536",
    "1239859",
    "1235247",
    "1235231",
    "1232091",
    "1232055",
    "1231632",
    "1230469",
    "1230321",
    "1228207",
    "1226498",
    "1225110",
    "1219775",
    "1219219",
    "1219128",
    "1218162",
    "1217544",
    "1210990",
    "1209390",
    "1208776",
    "1208775",
    "1207700",
    "1204350",
    "1199737",
    "1199665",
    "1197590",
    "1195242",
    "1194410",
    "1187647",
    "1186281",
    "1184059",
    "1182700",
    "1179743",
    "1178751",
    "1177516",
    "1176827",
    "1174782",
    "1173694",
    "1171394",
    "1169485",
    "1167959",
    "1167872",
    "1165945",
    "1162778",
    "1161767",
    "1154337",
    "1149826",
    "1149505",
    "1146490",
    "1140402",
    "1135719",
    "1134514",
    "1124227",
    "1118086",
    "1112374",
    "1109851",
    "1105386",
    "1100252",
    "1094736",
    "1061578",
    "1061094",
    "1055887",
    "1052560",
    "1045926",
    "1043118",
    "1041818",
    "1034964",
    "1034534",
    "1034499",
    "1034063",
    "1034038",
    "1033580",
    "1032246",
    "1022241",
    "1022231",
    "1019630",
    "1006102",
    "1000540",
    "999900",
    "998606",
    "985024",
    "976753",
    "976521",
    "975444",
    "974389",
    "973759",
    "969880",
    "968123",
    "967096",
    "966514",
    "956100",
    "950799",
    "948956",
    "947365",
    "946571",
    "944415",
    "941241",
    "933679",
    "930586",
    "928222",
    "925874",
    "924888",
    "922719",
    "920031",
    "912159",
    "904846",
    "896666",
    "894561",
    "892485",
    "891452",
    "887792",
    "883895",
    "883884",
    "881974",
    "878346",
    "875046",
    "870627",
    "869505",
    "869496",
    "866522",
    "861090",
    "860312",
    "859955",
    "859276",
    "858128",
    "856371",
    "854848",
    "847991",
    "845820",
    "844661",
    "844660",
    "842871",
    "839933",
    "838681",
    "837985",
    "837489",
    "836343",
    "833792",
    "833791",
    "833774",
    "827937",
    "825578",
    "823941",
    "818337",
    "816607",
    "814565",
    "813187",
    "801949",
    "801072",
    "793345",
    "792151",
    "789871",
    "786382",
    "785490",
    "783358",
    "767197",
    "765980",
    "764076",
    "759922",
    "759342",
    "755555",
    "754861",
    "751712",
    "749113",
    "748232",
    "745549",
    "741050",
    "738574",
    "728738",
    "727422",
    "726451",
    "725156",
    "721273",
    "721236",
    "721199",
    "716279",
    "715919",
    "715612",
    "715378",
    "715376",
    "715336",
    "713479",
    "711734",
    "710398",
    "710359",
    "707195",
    "706008",
    "705826",
    "705483",
    "704128",
    "703159",
    "701661",
    "701029",
    "700533",
    "700208",
    "697359",
    "697248",
    "694689",
    "692955",
    "691645",
    "690229",
    "689962",
    "688668",
    "688556",
    "687311",
    "686782",
    "685799",
    "684646",
    "683286",
    "683146",
    "682638",
    "679942",
    "679742",
    "675943",
    "675866",
    "674737",
    "674483",
    "674443",
    "673703",
    "672885",
    "672085",
    "670531",
    "669507",
    "668577",
    "667340",
    "666449",
    "664077",
    "663315",
    "660726",
    "657603",
    "656891",
    "656343",
    "654072",
    "653102",
    "651060",
    "649671",
    "648789",
    "648568",
    "648398",
    "647473",
    "646655",
    "645563",
    "644594",
    "643781",
    "643758",
    "643554",
    "641346",
    "641341",
    "641340",
    "638598",
    "637002",
    "633812",
    "632264",
    "631462",
    "628179",
    "628129",
    "623538",
    "623153",
    "622801",
    "621429",
    "620691",
    "617128",
    "613751",
    "613498",
    "613126",
    "612029",
    "612006",
    "611955",
    "611161",
    "606170",
    "605357",
    "605222",
    "605197",
    "597564",
    "595451",
    "590945",
    "590755",
    "590558",
    "588317",
    "587438",
    "586842",
    "585352",
    "584285",
    "583890",
    "583299",
    "582613",
    "582005",
    "580070",
    "579843",
    "579629",
    "578694",
    "578541",
    "578179",
    "576347",
    "574253",
    "571918",
    "571344",
    "570835",
    "569645",
    "569331",
    "567362",
    "567039",
    "566514",
    "565740",
    "565564",
    "565549",
    "565104",
    "565035",
    "561937",
    "561586",
    "561361",
    "559762",
    "559729",
    "555985",
    "554004",
    "550246",
    "549680",
    "549419",
    "546559",
    "546254",
    "545685",
    "543435",
    "541844",
    "539597",
    "537143",
    "536996",
    "536955",
    "536540",
    "534967",
    "534962",
    "531406",
    "530594",
    "529761",
    "529748",
    "529746",
    "528800",
    "526293",
    "524629",
    "524468",
    "521264",
    "517642",
    "516781",
    "516502",
    "515521",
    "513149",
    "511899",
    "509986",
    "507552",
    "505521",
    "501837",
    "501580",
    "501421",
    "499686",
    "497696",
    "497164",
    "493503",
    "493124",
    "491283",
    "490714",
    "489100",
    "488800",
    "486635",
    "481128",
    "479829",
    "478459",
    "477605",
    "476541",
    "469456",
    "469421",
    "466572",
    "462743",
    "461500",
    "460969",
    "460356",
    "460050",
    "459638",
    "459007",
    "458864",
    "456957",
    "455986",
    "455937",
    "455164",
    "451641",
    "450955",
    "450954",
    "449235",
    "445639",
    "444915",
    "443396",
    "443386",
    "441968",
    "439938",
    "437791",
    "435799",
    "435628",
    "435380",
    "435081",
    "435013",
    "434726",
    "434327",
    "434301",
    "434174",
    "433778",
    "433422",
    "432520",
    "431544",
    "431098",
    "430613",
    "429392",
    "429302",
    "429021",
    "428981",
    "428602",
    "428087",
    "426849",
    "424646",
    "423789",
    "422330",
    "421423",
    "419911",
    "419598",
    "419344",
    "418864",
    "418144",
    "417770",
    "417545",
    "417259",
    "416766",
    "414961",
    "411657",
    "410312",
    "407817",
    "407325",
    "406488",
    "406157",
    "405108",
    "404856",
    "404081",
    "403959",
    "403179",
    "401380",
    "401213",
    "401172",
    "394791",
    "393466",
    "392866",
    "391977",
    "391386",
    "388664",
    "387406",
    "385615",
    "382885",
    "382477",
    "380828",
    "379272",
    "378082",
    "376027",
    "374292",
    "369440",
    "368909",
    "366325",
    "363383",
    "363044",
    "362880",
    "361148",
    "359418",
    "358266",
    "357337",
    "349733",
    "349076",
    "347261",
    "344267",
    "343999",
    "342675",
    "342101",
    "337801",
    "336829",
    "336193",
    "336029",
    "335963",
    "334500",
    "332990",
    "332973",
    "332740",
    "331257",
    "329693",
    "325942",
    "325891",
    "324570",
    "322617",
    "320989",
    "319819",
    "318514",
    "318474",
    "318245",
    "317081",
    "313718",
    "311756",
    "311742",
    "311223",
    "310135",
    "309217",
    "307866",
    "307089",
    "306625",
    "305585",
    "303597",
    "302238",
    "301888",
    "299138",
    "298784",
    "298281",
    "295930",
    "295098",
    "295020",
    "293611",
    "293323",
    "292284",
    "290125",
    "288606",
    "285395",
    "280536",
    "280014",
    "279923",
    "279022",
    "276311",
    "276295",
    "275475",
    "275173",
    "274205",
    "273968",
    "272983",
    "266702",
    "266600",
    "266338",
    "266122",
    "265915",
    "265140",
    "265084",
    "262123",
    "260348",
    "259810",
    "259594",
    "257307",
    "254592",
    "254544",
    "252803",
    "252602",
    "250855",
    "250622",
    "250123",
    "249951",
    "249919",
    "248648",
    "248352",
    "245897",
    "242840",
    "242829",
    "240625",
    "238041",
    "236107",
    "236100",
    "234243",
    "233047",
    "232919",
    "230214",
    "230153",
    "228673",
    "228205",
    "227632",
    "226301",
    "226037",
    "225882",
    "223440",
    "222274",
    "221855",
    "221154",
    "220701",
    "217769",
    "214004",
    "212763",
    "211847",
    "210657",
    "208427",
    "206010",
    "205946",
    "204683",
    "203686",
    "203225",
    "201056",
    "200208",
    "199751",
    "199207",
    "198233",
    "197956",
    "196843",
    "196078",
    "195420",
    "194319",
    "193332",
    "193321",
    "191239",
    "190655",
    "190515",
    "188448",
    "188318",
    "186371",
    "185905",
    "184155",
    "182689",
    "181826",
    "179596",
    "179135",
    "177175",
    "176170",
    "175946",
    "175415",
    "172520",
    "169388",
    "166836",
    "163912",
    "162369",
    "161109",
    "160200",
    "160144",
    "159946",
    "158757",
    "158209",
    "155730",
    "154808",
    "150025",
    "149178",
    "148624",
    "145421",
    "145405",
    "144517",
    "143663",
    "143021",
    "142898",
    "142183",
    "142102",
    "140267",
    "139912",
    "136714",
    "136676",
    "136633",
    "133465",
    "129986",
    "129480",
    "127909",
    "126379",
    "126309",
    "124123",
    "122752",
    "122253",
    "120313",
    "118683",
    "117114",
    "115107",
    "113536",
    "112738",
    "112298",
    "112288",
    "111176",
    "109016",
    "105613",
    "103649",
    "102695",
    "102380",
    "102057",
    "101611",
    "98554",
    "98168",
    "97278",
    "96463",
    "96264",
    "95790",
    "94270",
    "91337",
    "91242",
    "91190",
    "87314",
    "86770",
    "85686",
    "84973",
    "84833",
    "80713",
    "79107",
    "79021",
    "78681",
    "77976",
    "76854",
    "76828",
    "75158",
    "75133",
    "72352",
    "72001",
    "71074",
    "69792",
    "69486",
    "68851",
    "67595",
    "66183",
    "65548",
    "65279",
    "64926",
    "64232",
    "64068",
    "63798",
    "62395",
    "61883",
    "61071",
    "59248",
    "59173",
    "58830",
    "58788",
    "57882",
    "57563",
    "57451",
    "57420",
    "57022",
    "56701",
    "54940",
    "54479",
    "53927",
    "53579",
    "52282",
    "50959",
    "50511",
    "48332",
    "47752",
    "47159",
    "43464",
    "43156",
    "43114",
    "41577",
    "41250",
    "40988",
    "39841",
    "38933",
    "38646",
    "38121",
    "37694",
    "37660",
    "36539",
    "33654",
    "32157",
    "29086",
    "27795",
    "27771",
    "27493",
    "25894",
    "23858",
    "20573",
    "19261",
    "17978",
    "15438",
    "13610",
    "12460",
    "10212",
    "8131",
    "5704",
    "3658",
    "3246",
    "2212",
    "2056",
]
BOT_USERNAME = "release-mgmt-account-bot@mozilla.tld"


class FixSeverityUnderestimated(BzCleaner):
    no_bugmail: bool = True

    def description(self):
        return "Clear needinfos from severity_underestimated"

    def handle_bug(self, bug, data):
        bugid = str(bug["id"])
        if bugid not in AFFECTED_BUG_IDS:
            return None

        bot_needinfo_today = [
            flag
            for flag in bug["flags"]
            if flag["name"] == "needinfo"
            and flag["status"] == "?"
            and flag["setter"] == BOT_USERNAME
            and flag["creation_date"].startswith("2022-10-17")
        ]

        assert len(bot_needinfo_today) == 1, f"Unexpected needinfo count for {bugid}"

        if bug["creation_time"] > "2019" and len("duplicates") > 0:
            bug["summary"] = "keep needinfo"
        else:
            self.autofix_changes[bugid] = {
                "flags": [
                    {
                        "id": flag["id"],
                        "status": "X",
                    }
                    for flag in bot_needinfo_today
                ]
            }
            bug["summary"] = "clear needinfo"

        return bug

    def get_bugs(self, date="today", bug_ids=..., chunk_size=None):
        bugs = super().get_bugs(date, bug_ids, chunk_size)

        for bugid in AFFECTED_BUG_IDS:
            if bugid not in bugs:
                bugs[bugid] = {"id": bugid, "summary": "no needinfo"}

        return bugs

    def get_bz_params(self, date):
        fields = ["flags", "creation_time", "duplicates"]
        return {
            "include_fields": fields,
            "f1": "setters.login_name",
            "o1": "equals",
            "v1": BOT_USERNAME,
            "f2": "longdesc",
            "o2": "substring",
            "v2": "https://wiki.mozilla.org/Release_Management/autonag#severity_underestimated.py",
        }


if __name__ == "__main__":
    FixSeverityUnderestimated().run()

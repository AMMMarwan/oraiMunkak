Ebben az öszefoglalóban leírom először a parancsot az után pedig, hogy mire "való"

table>(tr>td*4)*4

- 4x4-es táblázat

<style>
        table{
            border: 1px solid;
            width: 400px;
            height: 400px;
        }
    </style>

- border

 <style>
        .sakkTable{
            border: 1px solid;
            width: 400px;
            height: 400px;
        }
    </style>

- tábla osztálya

        tr:nth-child(odd) td:nth-child(even),
        tr:nth-child(even) td:nth-child(odd) {
            background-color: black;
        }

- sakk színek hozzáadása

- "tr" =sor

table.sakkTable>(tr>td*8)*8

- osztaly tabla keszités 8x8


        .trSakk:nth-child(odd) .tdSakk:nth-child(even),
        .trSakk:nth-child(even) .tdSakk:nth-child(odd) {
            background-color: black;
        }

table.sakkTable>(tr.trSakk>td.tdSakk*4)*4

- az egész 4x4-es sakk csoportos/osztályos

table.sakkTable>(tr>th*4)(tr.trSakk>td.tdSakk*4)*4

- fejléc cella

table.sakkTable>(tr>th*4)(tr.trSakk>td.tdSakk*4)*4(rz>th*4)*1


- alulra is

table.sakkTable>(tr>th*4)(tr.trSakk>th*1td.tdSakk*4th)*4(tr>th*4)*1

- kb alap sakk 4x4-es

        th{
            border: 1px solid;
        }

- keretet ad a számok/betuknek

        .thFejen{
            rotate: 180deg;
        }

- számok/betuknek fejre forditása

______________________________________________________________________

table.sakkTable>(tr>th.thFejen*6)(tr.trSakk>th*1td.tdSakk*4th.thFejen*1)*4(tr>th*6)*1

- fejléc csoport berakva

table.sakkTable>(tr>th.thFejen*10)(tr.trSakk>th*1td.tdSakk*8th.thFejen*1)*8(tr>th*10)*1

- 8x8 sakk

        .trSakk:nth-child(odd) .tdSakk:nth-child(even),
        .trSakk:nth-child(even) .tdSakk:nth-child(odd) {
            background-color: black;
            border: 1px solid;
            width: 50px;
            height: 50px;
        }
        .trSakk:nth-child(odd) .tdSakk:nth-child(odd),
        .trSakk:nth-child(even) .tdSakk:nth-child(even) {
            background-color: lightblue;
            border: 1px solid;
            width: 50px;
            height: 50px;
        }
        th{
            border: 1px solid;
            width: 50px;
            height: 50px;
        }
        .thFejen{
            rotate: 180deg;
            width: 50px;
            height: 50px;
        }

- cellák rendezése
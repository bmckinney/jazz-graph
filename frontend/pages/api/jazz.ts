import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {

    const {body, method} = req
    console.log(body)
    const options = {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            "Content-Type": "application/json",
            Authorization: 'Basic ' + process.env.ONGDB_BASIC_AUTH
        },
        //body: '{"statements":[{"statement":"MATCH (person:Person {name: \'Roy Haynes\'})-[part:PARTICIPATED_IN]->(performance:Performance)-[hp:HAS_PLACE]->(place:Place {name: \'Van Gelder Studio\'}) RETURN DISTINCT hp.begin as dates, place.name as place, count(performance) as performances ORDER BY hp.begin ASC","resultDataContents":["row"]}]}'
        body: '{"statements":[{"statement":"' + body + '","resultDataContents":["row"]}]}'
    };

    function convert_row_data(json) {
        let return_value: any = {}
        let results: any = []
        let labels = json[0].columns
        for (let i = 0; i < json[0].data.length; i++) {
            console.log(json[0].data[i].row);
            let item = '{ '
            for (let j = 0; j < labels.length; j++) {
                item = item + '"' + labels[j] + '": "' + json[0].data[i].row[j] + '"'
                if (j < labels.length-1) { item = item + "," }
            }
            item = item + '}'
            results.push(JSON.parse(item))
            return_value.results = results
        }
        return return_value
    }

    switch (method) {
        case 'POST':
            try {
                const cypher_response = await fetch(
                    process.env.ONGDB_URL + '/db/data/transaction/commit', options);
                const data = await cypher_response.json()
                let json_results = convert_row_data(data.results)
                res.status(200).json(json_results)
                break
            } catch (err) {
                //console.log(err)
                res.status(500).json(err)
                break
            }
        default:
            res.setHeader('Allow', ['GET', 'PUT'])
            res.status(405).end(`Method ${method} Not Allowed`)
    }
}

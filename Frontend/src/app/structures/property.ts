export interface propertyStructure {

    _id: myId,
    name: string,
    description: string,
    greenscore: number,
    address: string,
    propertyvalues: propertyValues
}

interface myId {
    $oid: string
}

interface propertyValues {
    energy: string,
    co2: number,
    waste: number,
    cleanenergy: number,
    area: number,
    propertytype: string
}
const dbName = "vehicles";
const conn = new Mongo();
const db = conn.getDB(dbName);
use vehicles;

const collectionSettings = [
    {
        name: "components",
        shardKey: "component",
        indexFields: [
            "component"
        ]
    },
];

sh.enableSharding(dbName);

collectionSettings.forEach((collection) => {
    const collectionName = collection.name;
    const shardKey = collection.shardKey;
    const indexFields = collection.indexFields;

    db.createCollection(collectionName);
    if (indexFields !== undefined) {
        indexFields.forEach((field) => {
            db[collectionName].createIndex({[field]: -1});
        })
    }
    if (shardKey !== undefined) {
        sh.shardCollection(`${dbName}.${collectionName}`, {[shardKey]: "hashed"});
    }

});
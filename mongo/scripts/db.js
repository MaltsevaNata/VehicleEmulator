const dbName = "vehicles";
const conn = new Mongo();
const db = conn.getDB(dbName);

const collectionSettings = [
    {
        name: "components",
        shardKey: "country"
    },
];

sh.enableSharding(dbName);

collectionSettings.forEach((collection) => {
    const collectionName = collection.name;
    const shardKey = collection.shardKey;
    const indexFields = collection.indexFields;

    db.createCollection(collectionName);
    if (shardKey !== undefined) {
        sh.shardCollection(`${dbName}.${collectionName}`, {[shardKey]: "hashed"});
    }
    if (indexFields !== undefined) {
        indexFields.forEach((field) => {
            db[collectionName].createIndex({[field]: -1});
        })
    }
});
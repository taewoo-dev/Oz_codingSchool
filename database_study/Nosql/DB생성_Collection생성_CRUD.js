use test_database // (1).데이터베이스 생성 or 전환 
db // (2). 현재 connect된 데이터베이스 조회 
show dbs // (3). 모든 데이터베이스 조회 
db.dropDatabase() // (4) 현재 데이터베이스 삭제 
db.stats() // (5).현재 데이터베이스 상태 조회 
// (6). 데이터베이스 컬랙션 생성 
db.createCollection("users", { capped: false }) // (7). 크기 조정x 
db.createCollection("log", { capped: true, size: 100000}) // (8). 크기 조정 O 
// (9). Json 문서의 유효성 검사가 있는 컬랙션 생성 
db.createCollection("contacts",{
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["phone"], // (10).phone Field 필수 
            properties: {
                phone: {
                    bsonType: "string",
                    description: "must be a string and is required"
                },
                email: {
                    bsonType: "string",
                    pattern: "@mongodb\.com$", // (11). email Field 특정 패턴에 따라야 한다 
                    description: "must be a string and match the reqular expression pattern"
                }
            }
        }
    }
})
// (12). 특정 스토리지의 엔진 옵션을 사용하는 컬렉션 생성 
db.createCollection("myData", {
    storageEngine: {
        wiredTiger: {
            configString: "block_compressor=zlib"
        }
    }
})
// (13). 컬렉션 목록 조회  
show collections
// (14). 컬렉션 이름 변경 
db.users.renameCollection("customers")
show collections
// (15). 컬렉션 삭제 
db.customers.drop()
show collections
show collections

// CREATE document
// C-1) 단일 문서 삽입 
db.users.insertOne({
    name: "taewoo",
    age: 26,
    status: "pending"
})
db.users.insertOne({
    name: "Alice",
    age: 30,
    address: "123 Maple St"
})
// C-2) 여러 문서 삽입 - 리스트 형태로 입력 
db.users.insertMany([
    { 
        name: "Bob",
        age: 25,
        address: "456 Oak St"},
    {
        name: "Charlie",
        age: 35,
        address: "789 Pins St"
    }
])

// READ document
// R-1) 모든 문서 조회 
db.users.find({})
// R-2) 특정 필드 조회 
db.users.find({}, { name: 1, address: 1}) // name과 address 출력 
// R-3) 조건에 맞는 문서 조회 
db.users.find({ address: "Seoul"})

// UPDATE document
// U-1) 특정 문서 업데이트 
db.users.updateOne(
    { name: "taewoo"},
    { $set: { address: "Seoul"} }
)
// U-2) 여러 문서 업데이트 
db.users.updateMany(
    { age: 25 },
    { $set: {  address: "Busan"} }
)

// DELETE document
// D-1) 특정 문서 삭제 
db.users.deleteOne({ name: "Bob"})
db.users.deleteMany({ address: "Busan"})
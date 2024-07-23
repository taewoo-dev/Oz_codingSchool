// CRUD 연습
// (1). sports 컬렉션에 name: "Football", players: 11인 문서를 삽입하세요.
db.createCollection("sports", { capped: false })
db.sports.insertOne({
    name: "Football",
    palyers: 11
})
db.sports.find()
// (2). products 컬렉션에서 price가 500보다 작거나 같은 모든 문서를 찾으세요.
db.createCollection("products",{ capped: false})
db.products.insertMany([
    {
        name: "아이폰",
       price: 1000
    },
    {
        name: "갤럭시폰",
        price: 600
    },
    {
        name: "LG폰",
        price: 400
    }
])
db.products.find({
    price: { $lte: 500}
})

// (3). books 컬렉션에서 author가 "John Doe"인 모든 문서를 찾으세요.
db.createCollection("books", { capped: false })
db.books.insertMany([
    {
        name: "책1",
        author: "John Doe"
    },
    {
        name: "책2",
        author: "doctor j"
    }
])
db.books.find({ author: "John Doe"})
// (4). 업데이트 orders 컬렉션에서 status가 "Pending"인 모든 문서를 "Complete"로 변경하세요.
db.createCollection("orders", { capped: false })
show collections
db.orders.insertMany([
    {
        order_id: 1,
        amount: 10000,
        status: "Pending"
    },
    {
        order_id: 2,
        amount: 20000,
        status: "Pending"
    },
    {
        order_id: 3,
        amount: 30000,
        status: "sales"
    }
])
db.orders.find({ status: "Pending"})
db.orders.updateMany(
    {
        status: "Pending"
    },
    {
        $set: { status: "Complete"}
    }
)
db.orders.find()
// (5). movies 컬렉션에서 genre가 "comedy"인 모든 문서의 rating을 5로 변경하세요.
db.movies.insertMany([
    {
        movie_id: 1,
        genre: "comedy",
        rating: 1
    },
    {
        movie_id: 2,
        genre: "comedy",
        rating: 2
    },
    {
        movie_id: 3,
        genre: "action",
        rating: 5
    }
])
db.movies.find()
db.movies.updateMany(
    { 
        genre: "comedy"
    },
    {
        $set: { rating: 5}
    }
)
// (6). customers 컬렉션에서 age가 30 미만인 모든 문서를 삭제하세요.
db.customers.insertMany([
    {
        customer_id: 1,
        age: 10
    },
    {
        customer_id: 2,
        age: 15
    },
    {
        customer_id: 3,
        age: 30
    },
    {
        customer_id: 4,
        age: 40
    },
])
db.customers.find()
db.customers.deleteMany(
    {
        age: { $lt: 30 }
    }
)
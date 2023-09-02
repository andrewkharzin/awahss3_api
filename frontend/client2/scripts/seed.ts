const { PrismaClient } = require("@prisma/client");

const db = new PrismaClient();

async function main() {
    try {
        await db.category.createMany({
            data: [
               { name: "Notes"},
               { name: "Tasks"},
               { name: "Projects"},
               { name: "Flights"},
               { name: "Activites"},
               { name: "Users"},
               { name: "Airlines"},
           ]
       })
    
   } catch (error) {
     console.error("Error seeding default categories", error)
   } finally {
       await db.$disconnect();
   }
}
    

main();

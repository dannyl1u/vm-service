import express from "express";
import { commandOptions, createClient } from "redis";

const subscriber = createClient();
subscriber.connect();

const app = express();
app.use(express.json());

async function main() {
    while(1) {
        const response = await subscriber.brPop(
            commandOptions({ isolated: true }),
            'upload-queue',
            0
        );
        console.log(response);
        console.log(response?.element)

        // TODO: download the file named response?.element.ts from the gcp bucket
        // TODO spin up vm instance with the downloaded file
    }
}

main();

app.listen(3001, () => console.log("Server is running on port 3001"));
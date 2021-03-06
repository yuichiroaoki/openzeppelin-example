# Smart Contract Dev Template
Template for smart contract development using Typescript & Hardhat

## Available Scripts

In the project directory, you can run:

### `yarn build`
Clears the cache and deletes all artifacts && Compiles the entire project, building all artifacts

### `yarn clean`
Clears the cache and deletes all artifacts

### `yarn compile`
Compiles the entire project, building all artifacts

### `npx hardhat node`
Starts a JSON-RPC server on top of Hardhat Network

### `yarn test`
Runs mocha tests

### `yarn coverage`
Implement a code coverage for tests

### `yarn account`
Show the list of accounts

### `yarn block-number`
Show the current block number

### `yarn balance (account's address)`
Show an account's balance 

## References
https://hardhat.org/guides/create-task.html

## Run fastapi
```console
chmod +x startup.sh
./startup.sh
uvicorn main:app --reload
```

## upload to cloud storage
https://github.com/google-github-actions/upload-cloud-storage

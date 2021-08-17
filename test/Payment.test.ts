import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/signers";
import { expect } from "chai";
import { ethers } from "hardhat";
import { Payment__factory, Payment } from "../typechain";

describe("Payment", () => {

	let Payment: Payment;
	let owner: SignerWithAddress;
	let addr1: SignerWithAddress;
	let addr2: SignerWithAddress;
	let addrs: SignerWithAddress[];

	const provider = ethers.provider

	beforeEach(async () => {
		[owner, addr1, addr2, ...addrs] = await ethers.getSigners();

		const PaymentFactory = (await ethers.getContractFactory(
			"Payment", owner
		)) as Payment__factory;
		Payment = await PaymentFactory.deploy();
		await Payment.deployed();

	})

});
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/security/PullPayment.sol";

contract Payment is PullPayment {

	function giveEther(address payee, uint256 amount) external payable {

		_asyncTransfer(payee, amount);

	}

}
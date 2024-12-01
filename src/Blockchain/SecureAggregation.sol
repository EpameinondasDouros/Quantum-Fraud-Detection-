// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureAggregation {
    struct Batch {
        uint256 batchStart;
        uint256 batchEnd;
        bytes32[] encryptedHashes;
    }

    Batch[] public batches;
    bytes32 public aggregatedQhash; // Variable to store the aggregated Qhash

    event BatchSubmitted(uint256 indexed batchStart, uint256 indexed batchEnd);
    event AggregatedQhashStored(bytes32 indexed qhash); // Event for storing the aggregated Qhash

    // Function to submit a batch of Qhashes
    function submitBatch(
        uint256 _batchStart,
        uint256 _batchEnd,
        bytes32[] memory _encryptedHashes
    ) public {
        batches.push(Batch(_batchStart, _batchEnd, _encryptedHashes));
        emit BatchSubmitted(_batchStart, _batchEnd);
    }

    // Function to store the aggregated Qhash
    function storeAggregatedQhash(bytes32 _aggregatedQhash) public {
        aggregatedQhash = _aggregatedQhash;
        emit AggregatedQhashStored(_aggregatedQhash);
    }

    // Function to retrieve the aggregated Qhash
    function getAggregatedQhash() public view returns (bytes32) {
        return aggregatedQhash;
    }

    // Function to retrieve all batches
    function getBatches() public view returns (Batch[] memory) {
        return batches;
    }
}


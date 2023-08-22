// votes push O(1)
var votes = [];

function addVote(candidate){
    votes.push(candidate);
}

// votes countVotes O(N)
function countVotes(votes){
    var tally = {};
    for(var i = 0; i < votes.length; i++){
        if(tally[votes[i]]){
            tally[votes[i]]++;
        }
        else {
            tally[votes[i]] = 1;
        }
    }
    return tally;
}

// advote O(1)
function adVote(candidate){
    if(votes[candidate]){
        votes[candidate]++;
    }
    else{
        votes[candidate] = 1;
    }
}

// 투표 배열 
addVote('Candidate A');
addVote('Candidate B');
addVote('Candidate A');
addVote('Candidate C');
addVote('Candidate A');

// countVotes  
var voteTally = countVotes(votes);
console.log('Vote Tally:', voteTally);

// adVote  
adVote('Candidate B');
adVote('Candidate B');
adVote('Candidate C');
adVote('Candidate C');

console.log('Updated Votes:', votes);
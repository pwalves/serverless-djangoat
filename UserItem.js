
/**
 * Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * This file is licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License. A copy of
 * the License is located at
 *
 * http://aws.amazon.com/apache2.0/
 *
 * This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
*/
var AWS = require("aws-sdk");

AWS.config.loadFromPath('./config.json');

AWS.config.update({
    region:'us-east-2',
    endpoint: "https://dynamodb.us-east-2.amazonaws.com"
    
});

var docClient = new AWS.DynamoDB.DocumentClient();

    var params = {
        TableName: "SWAT-USERS-DB",
       
    };


var docClient = new AWS.DynamoDB.DocumentClient();

var table = "SWAT-USERS-DB";

var username = "Birdy";
var userId = "004";

var params = {
    TableName:table,
    Item:{
        "userId": userId,
        "username": username
    }
};

console.log("Adding a new item...");
docClient.put(params, function(err, data) {
    if (err) {
        console.error("Unable to add item. Error JSON:", JSON.stringify(err, null, 2));
    } else {
        console.log("Added item:", JSON.stringify(data, null, 2));
    }
});

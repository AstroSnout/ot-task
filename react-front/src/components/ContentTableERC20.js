import React from 'react';
import Table from 'react-bootstrap/Table';

const ContentTableERC20 = (props) => {
    console.log(props)
    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>Wallet Address</th>
                    <th>Smart Contract Address</th>
                    <th>Balance</th>
                    <th>Block Number</th>
                    <th>Timestamp</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{props.data.address}</td>
                    <td>{props.data.token_address}</td>
                    <td>{props.data.token_balance}</td>
                    <td>{props.data.block_number}</td>
                    <td>{props.data.timestamp}</td>
                </tr>
            </tbody>
        </Table>
    );
}

export default ContentTableERC20;
import React from 'react';
import Table from 'react-bootstrap/Table';

const ContentTable = (props) => {
    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                    <th>Wallet Address</th>
                    <th>Balance in ETH</th>
                    <th>Block Number</th>
                    <th>Timestamp</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{props.data.address}</td>
                    <td>{props.data.ether_balance}</td>
                    <td>{props.data.block_number}</td>
                    <td>{props.data.timestamp}</td>
                </tr>
            </tbody>
        </Table>
    );
}

export default ContentTable;
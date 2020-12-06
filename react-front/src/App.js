import React, { useState } from 'react';
// Bootstrap
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import Button from 'react-bootstrap/Button';
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
// Local imports
import ContentTable from './components/ContentTable';
import ContentTableBalance from './components/ContentTableBalance';
import ContentTableERC20 from './components/ContentTableERC20';
import Loading from './components/Loading';
import Error from './components/Error';
// CSS
import './App.css';


const App = () => {
  // Form Fields
  const [addressTx, setAddressTx] = useState('');
  const [blockNo, setBlockNo] = useState('');
  const [addressBal, setAddressBal] = useState('');
  const [dateBal, setDateBal] = useState('');
  const [addressERC20Bal, setAddressERC20Bal] = useState('');
  const [tokenAddress, setTokenAddress] = useState('')
  const [dateERC20Bal, setDateERC20Bal] = useState('');
  // States
  const [isError, setIsError] = useState(false);
  const [errorMsg, setErrorMsg] = useState('Generic Error');
  const [isLoaded, setIsLoaded] = useState(true);
  const [txData, setTxData] = useState([]);
  const [isShowTx, setIsShowTx] = useState(false);
  const [balData, setBalData] = useState([]);
  const [isShowBal, setIsShowBal] = useState(false);
  const [erc20BalData, setERC20BalData] = useState([]);
  const [isShowERC20Bal, setIsShowERC20Bal] = useState(false);

  function onClickTx() {
    getTransactions()
    setIsShowTx(true)
    setIsShowBal(false)
    setIsShowERC20Bal(false)
  };

  function onClickBal() {
    getBalance()
    setIsShowTx(false)
    setIsShowBal(true)
    setIsShowERC20Bal(false)
  }

  function onClickERC20Bal() {
    getERC20Balance()
    setIsShowTx(false)
    setIsShowBal(false)
    setIsShowERC20Bal(true)
  }

  function getTransactions() {
    setIsLoaded(false)
    setIsError(false)
    setTxData([])
    fetch(`http://127.0.0.1:5001/api/get_transactions?address=${addressTx}&blocknumber=${blockNo}`)
      .then(res => res.json())
      .then(
        (result) => {
          if (result.hasOwnProperty("error")) { 
            setErrorMsg(result.error); 
            setIsError(true); 
          }
          else { 
            setIsError(false);
            setTxData(result) 
          }
          setIsLoaded(true);
        },
        (error) => {
          console.log(error)
          setIsLoaded(true);
          setIsError(true);
        }
      )
  }

  function getBalance() {
    setIsLoaded(false)
    setIsError(false);
    setBalData([])
    let url = `http://127.0.0.1:5001/api/get_balance?address=${addressBal}`
    if (dateBal !== '') {
      url += `&date=${dateBal}`
    }
    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          if (result.hasOwnProperty("error")) { 
            setErrorMsg(result.error); 
            setIsError(true); 
          }
          else { 
            setIsError(false);
            setBalData(result) 
          }
          setIsLoaded(true);
        },
        (error) => {
          console.log(error)
          setIsLoaded(true);
          setIsError(true);
        }
      )
  }

  function getERC20Balance() {
    setIsLoaded(false)
    setIsError(false);
    setERC20BalData([])
    let url = `http://127.0.0.1:5001/api/get_erc20_balance?address=${addressERC20Bal}&token=${tokenAddress}`
    if (dateERC20Bal !== '') {
      url += `&date=${dateERC20Bal}`
    }
    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          if (result.hasOwnProperty("error")) { 
            setErrorMsg(result.error); 
            setIsError(true); 
          }
          else { 
            setIsError(false);
            setERC20BalData(result) 
          }
          setIsLoaded(true);
        },
        (error) => {
          console.log(error)
          setIsLoaded(true);
          setIsError(true);
        }
      )
  }


  return (
    <Container fluid id='main'>
      <Tabs defaultActiveKey="get-tx" id="uncontrolled-tab-example">

        {/* Transactions Tab */}
        <Tab eventKey="get-tx" title="Transactions">
          <Form inline>
            {/* Wallet Address */}
            <Form.Label htmlFor="inlineFormAddress" srOnly>
              Wallet Address
            </Form.Label>
            <Form.Control
              className="mb-2 mr-sm-2"
              id="inlineFormAddress"
              placeholder="Wallet Address"
              value={addressTx}
              onChange={event => setAddressTx(event.target.value)}
            />
            {/* Block number */}
            <Form.Label htmlFor="inlineFormBlockNo" srOnly>
              Block Number
            </Form.Label>
            <FormControl 
              className="mb-2 mr-sm-2"
              id="inlineFormBlockNo" 
              placeholder="Block Number" 
              value={blockNo}
              onChange={event => setBlockNo(event.target.value)}
            />
            {/* Submit button */}
            <Button 
              type="button" 
              className="mb-2 mr-sm-2"
              onClick={onClickTx}
            >
              Submit
            </Button>
          </Form>
        </Tab>

        {/* Balance Tab */}
        <Tab eventKey="balance" title="Balance">
          <Form inline>
            {/* Wallet Address */}
            <Form.Label htmlFor="inlineFormAddressBal" srOnly>
              Wallet Address
            </Form.Label>
            <Form.Control
              className="mb-2 mr-sm-2"
              id="inlineFormAddressBal"
              placeholder="Wallet Address"
              value={addressBal}
              onChange={event => setAddressBal(event.target.value)}
            />
            {/* Balance for Date */}
            <Form.Label htmlFor="inlineFormDateBal" srOnly>
              Date
            </Form.Label>
            <FormControl 
              className="mb-2 mr-sm-2"
              id="inlineFormDateBal" 
              placeholder="Date as YYYY-MM-DD" 
              value={dateBal}
              onChange={event => setDateBal(event.target.value)}
            />
            {/* Submit button */}
            <Button 
              type="button" 
              className="mb-2 mr-sm-2"
              onClick={onClickBal}
            >
              Submit
            </Button>
          </Form>
        </Tab>

        {/* ERC20 Balance Tab */}
        <Tab eventKey="erc20-balance" title="ERC20 Balance">
          <Form inline>
            {/* Wallet Address */}
            <Form.Label htmlFor="inlineFormAddressERC20Bal" srOnly>
              Wallet Address
            </Form.Label>
            <Form.Control
              className="mb-2 mr-sm-2"
              id="inlineFormAddressERC20Bal"
              placeholder="Wallet Address"
              value={addressERC20Bal}
              onChange={event => setAddressERC20Bal(event.target.value)}
            />
            {/* Smart contract Address */}
            <Form.Label htmlFor="inlineFormTokenAddress" srOnly>
              Wallet Address
            </Form.Label>
            <Form.Control
              className="mb-2 mr-sm-2"
              id="inlineFormTokenAddress"
              placeholder="Smart Contract Address"
              value={tokenAddress}
              onChange={event => setTokenAddress(event.target.value)}
            />
            {/* Balance for Date */}
            <Form.Label htmlFor="inlineFormDateERC20Bal" srOnly>
              Date
            </Form.Label>
            <FormControl 
              className="mb-2 mr-sm-2"
              id="inlineFormDateERC20Bal" 
              placeholder="Date as YYYY-MM-DD" 
              value={dateERC20Bal}
              onChange={event => setDateERC20Bal(event.target.value)}
            />
            {/* Submit button */}
            <Button 
              type="button" 
              className="mb-2 mr-sm-2"
              onClick={onClickERC20Bal}
            >
              Submit
            </Button>
          </Form>
        </Tab>
      </Tabs>
      {
        isShowTx &&
        <ContentTable data={txData} />
      }
      {
        isShowBal &&
        <ContentTableBalance data={balData} />
      }
      {
        isShowERC20Bal &&
        <ContentTableERC20 data={erc20BalData} />
      }
      {
        !isLoaded &&
        <div className='center-this square-200'>
          <Loading className='square-200' />
        </div>
      }
      {
        isError &&
        <Error  errorMsg={errorMsg}/>
      }
    </Container>
  );
}

export default App;
const express = require('express');
const { exec } = require('child_process');
const app = express();

const PORT = process.env.PORT || 5000;

//middleware
app.use(express.json({ extended: false }));

app.get('/', (req, res) => {
  //res.redirect('/car');
});

app.get('/car', (req, res) => {
  // res.redirect('/car/price');
});

app.post('/car/price', async (req, res) => {
  const { car_company, car_model, car_state, car_year, car_mileage } = req.body;

  console.log(car_mileage);
  console.log(car_model);
  console.log(car_company);
  console.log(car_state);
  console.log(car_year);

  var str =
    'python carPricePredict.py ' +
    car_company +
    ' ' +
    car_model +
    ' ' +
    car_state +
    ' ' +
    car_year +
    ' ' +
    car_mileage;
  exec(str, (error, stdout, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
    }
    console.log(stdout);

    res.json(stdout);
  });
});
app.listen(PORT, () => {
  console.log(`server started on port ${PORT}`);
});

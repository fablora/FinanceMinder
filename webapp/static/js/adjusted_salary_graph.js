// Js script to generate adjusted salary trend graph

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('show-cpi-info').addEventListener('click', function() {
        fetch("/income-analysis/", {
            headers: {
                'X-Requested-with': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('latest_cpi').innerText = data.latest_cpi;
            document.getElementById('salary_cpi').innerText = data.salary_cpi;
            document.getElementById('real_salary').innerText = data.real_salary;
            document.getElementById('inflation_rate').innerText = data.inflation_rate;
            document.getElementById('cpi-info').style.display = 'block';

            const dates = data.salary_trend_data.map(item => item[0]);
            const adjusted_salaries = data.salary_trend_data.map(item => item[1]);

            const trace = {
                x: dates,
                y: adjusted_salaries,
                mode: 'lines+markers',
                line: { color: '#008ac5'},
                marker: { size: 8 },
                name: 'Adjusted Salary'
            };

            const layout = {
                title: 'Salary Trend Adjusted for Inflation',
                xaxis: { title: 'Date' },
                yaxis: { 
                    title: {
                        text: 'Adjusted Salary',
                        standoff: 20
                    },
                    tickformat: '$,.2f',
                    gridcolor: '#283442',
                    zerolinecolor: '#283442',
                    automargin: true
                },
                paper_bgcolor: '#1e1e1e',
                plot_bgcolor: '#1e1e1e',
                font: { color: '#f4f4f4' }
            };

            const config = { responsive: true};

            Plotly.newPlot('salary-trend-chart', [trace], layout, config);

            document.getElementById('line-chart-container').style.display = 'block';
        });
    });
});
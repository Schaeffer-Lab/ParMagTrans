extern crate uom;

use uom::si::f32::*;
use uom::si::length::meter;
use uom::si::velocity::meter_per_second;
use uom::fmt::DisplayStyle::Abbreviation;

fn main() {
    // Option 1: Create velocity directly from the constant
    let c = Velocity::new::<meter_per_second>(299_792_458.0);
    
    // Option 2: Calculate from length and time
    let length = Length::new::<meter>(299_792_458.0);
    let time = Time::new::<uom::si::time::second>(1.0);
    let c_calculated = length / time;
    
    // Format and display
    let formatted = c.into_format_args(meter_per_second, Abbreviation);
    println!("The speed of light is {}", formatted);
    
    let formatted2 = c_calculated.into_format_args(meter_per_second, Abbreviation);
    println!("The speed of light (calculated) is {}", formatted2);

    // Beta = n k_b T/(B^2/2 mu_0)
    let n = 1.0 * Length::new::<meter>(1.0).powi(3).recip(); // particle density in m^-3
    let formatted = n.into_format_args(meter.powi(3).recip(), Abbreviation);
    println!("Particle density n = {}", formatted);
}

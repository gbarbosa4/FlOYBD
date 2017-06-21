import transitfeed


schedule = transitfeed.Schedule()
schedule.AddAgency("Europe Agency", "http://iflyagency.com","Europe/Madrid","europe")

service_period = schedule.GetDefaultServicePeriod()
service_period.SetStartDate("20070101")
service_period.SetEndDate("20190101")
service_period.SetWeekdayService(True)
service_period.SetDateHasService('20070704', False)

lleida = schedule.AddStop(lng=0.6199348, lat=41.6183423, name="Lleida")
barcelona = schedule.AddStop(lng=2.0785566, lat=41.3947687, name="Barcelona")
paris = schedule.AddStop(lng=2.2071319, lat=48.8587737, name="Paris")
brussels = schedule.AddStop(lng=4.305179, lat=50.854954, name="Brussels")
amsterdam = schedule.AddStop(lng=4.7581896, lat=52.3745287, name="Amsterdam")
berlin = schedule.AddStop(lng=13.1452858, lat=52.5072095, name="Berlin")
viena = schedule.AddStop(lng=16.2396348, lat=48.2205994, name="Viena")
praga = schedule.AddStop(lng=14.325199, lat=50.0595849, name="Praga")
milan = schedule.AddStop(lng=9.1075211, lat=45.4627123, name="Milan")
roma = schedule.AddStop(lng=12.395572, lat=41.9099856, name="Roma")
florence = schedule.AddStop(lng=11.1707567, lat=43.7799367, name="Florence")



route_lleida = schedule.AddRoute(short_name="1", long_name="Route Lleida",route_type="Bus")
route_bcn = schedule.AddRoute(short_name="2", long_name="Route Barcelona",route_type="Bus")
route_paris = schedule.AddRoute(short_name="3", long_name="Route Paris",route_type="Bus")
route_brussels = schedule.AddRoute(short_name="4", long_name="Route Brusels",route_type="Bus")
route_amsterdam = schedule.AddRoute(short_name="5", long_name="Route Amsterdam",route_type="Bus")
route_berlin = schedule.AddRoute(short_name="6", long_name="Route Berlin",route_type="Bus")
route_viena = schedule.AddRoute(short_name="7", long_name="Route Viena",route_type="Bus")
route_praga = schedule.AddRoute(short_name="8", long_name="Route Praga",route_type="Bus")
route_milan = schedule.AddRoute(short_name="9", long_name="Route Milan",route_type="Bus")
route_roma = schedule.AddRoute(short_name="10", long_name="Route Roma",route_type="Bus")
route_florence = schedule.AddRoute(short_name="11", long_name="Route Florence",route_type="Bus")


#From Lleida
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Barcelona")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Paris")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Brusels")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Amsterdam")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Berlin")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Viena")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Praga")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Milan")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Roma")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_lleida.AddTrip(schedule, headsign="From Lleida To Florence")
trip.AddStopTime(lleida, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Barcelona
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Lleida")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='10:30:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Paris")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Brusels")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Amsterdam")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Berlin")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Viena")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Praga")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Milan")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Roma")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_bcn.AddTrip(schedule, headsign="From Barcelona To Florence")
trip.AddStopTime(barcelona, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Paris
trip = route_paris.AddTrip(schedule, headsign="From Paris To Barcelona")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Lleida")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Brusels")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Amsterdam")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Berlin")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Viena")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Praga")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Milan")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Roma")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_paris.AddTrip(schedule, headsign="From Paris To Florence")
trip.AddStopTime(paris, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Brusels
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Barcelona")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Paris")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Lleida")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Amsterdam")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Berlin")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Viena")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Praga")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Milan")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Roma")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_brussels.AddTrip(schedule, headsign="From Brusels To Florence")
trip.AddStopTime(brussels, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Amsterdam
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Barcelona")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Paris")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Brusels")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Lleida")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Berlin")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Viena")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Praga")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Milan")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Roma")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_amsterdam.AddTrip(schedule, headsign="From Amsterdam To Florence")
trip.AddStopTime(amsterdam, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Berlin
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Barcelona")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Paris")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Brusels")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Amsterdam")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Lleida")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Viena")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Praga")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Milan")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Roma")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_berlin.AddTrip(schedule, headsign="From Berlin To Florence")
trip.AddStopTime(berlin, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Viena
trip = route_viena.AddTrip(schedule, headsign="From Viena To Barcelona")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Paris")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Brusels")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Amsterdam")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Berlin")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Lleida")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Praga")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Milan")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Roma")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_viena.AddTrip(schedule, headsign="From Viena To Florence")
trip.AddStopTime(viena, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Praga
trip = route_praga.AddTrip(schedule, headsign="From Praga To Barcelona")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Paris")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Brusels")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Amsterdam")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Berlin")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Viena")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Lleida")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Milan")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Roma")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_praga.AddTrip(schedule, headsign="From Praga To Florence")
trip.AddStopTime(praga, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Milan
trip = route_milan.AddTrip(schedule, headsign="From Milan To Barcelona")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Paris")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Brusels")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Amsterdam")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Berlin")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Viena")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Praga")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Lleida")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Roma")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_milan.AddTrip(schedule, headsign="From Milan To Florence")
trip.AddStopTime(milan, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Roma
trip = route_roma.AddTrip(schedule, headsign="From Roma To Barcelona")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Paris")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Brusels")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Amsterdam")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Berlin")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Viena")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Praga")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Milan")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Roma")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')
trip = route_roma.AddTrip(schedule, headsign="From Roma To Florence")
trip.AddStopTime(roma, stop_time='09:00:00')
trip.AddStopTime(florence, stop_time='18:45:00')

#From Florence
trip = route_florence.AddTrip(schedule, headsign="From Florence To Barcelona")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(barcelona, stop_time='10:30:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Paris")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(paris, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Brusels")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(brussels, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Amsterdam")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(amsterdam, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Berlin")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(berlin, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Viena")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(viena, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Praga")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(praga, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Milan")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(milan, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Roma")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(roma, stop_time='18:45:00')
trip = route_florence.AddTrip(schedule, headsign="From Florence To Lleida")
trip.AddStopTime(florence, stop_time='09:00:00')
trip.AddStopTime(lleida, stop_time='18:45:00')



schedule.Validate()
schedule.WriteGoogleTransitFeed('google_transit_europe.zip')
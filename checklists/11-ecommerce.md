# Checklist: E-commerce

**OWASP Top 10:** A01, A03, A04
**Relacionado:** PCI DSS

## Pagos

- [ ] ¿Los pagos se procesan por un gateway externo (Stripe, PayPal)?
- [ ] ¿No se almacenan datos de tarjetas (PAN, CVV)?
- [ ] ¿PCI DSS compliance verificado?
- [ ] ¿Las transacciones tienen idempotencia?
- [ ] ¿El webhook de pago verifica firma?

## Carrito

- [ ] ¿El precio del producto se valida en backend?
- [ ] ¿La cantidad en carrito se valida en backend?
- [ ] ¿No se puede manipular el total del carrito?
- [ ] ¿Descuentos/cupones se validan en backend?
- [ ] ¿Los cupones tienen límite de uso?

## Órdenes

- [ ] ¿El usuario solo ve sus propias órdenes?
- [ ] ¿El estado de la orden no es manipulable?
- [ ] ¿La cancelación de orden es segura?
- [ ] ¿Los reembolsos requieren autorización?

## Inventario

- [ ] ¿El stock se valida antes de confirmar orden?
- [ ] ¿Race conditions en stock (overselling)?
- [ ] ¿Reserva de stock con timeout?

## Usuarios

- [ ] ¿Un usuario no puede ver órdenes de otro?
- [ ] ¿Las direcciones de envío se validan?
- [ ] ¿Historial de órdenes protegido?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| Price tampering | Modificar precio en request | ZAP + Manual |
| Coupon abuse | Uso múltiple de cupones | Manual |
| Order manipulation | Cambiar estado de orden | Manual |
| Refund abuse | Reembolsos fraudulentos | Manual |
